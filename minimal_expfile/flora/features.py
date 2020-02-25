#!/usr/bin/env python
# -*- coding: utf-8 -*-
#============================================================================
# Code: MOABB_AMFM_TSSF_feature
# Author: Jiachen XU <jiachen.xu.94@gmail.com>
#
# Last Update: 2019-11-25
#============================================================================

import os
import pdb
import copy
import yaml
import numpy as np
from matplotlib import pyplot as plt
import numba as nb

from scipy import signal
from scipy import linalg
from scipy.linalg import logm, eig

from mne.decoding import CSP
from mne import EvokedArray

from pyriemann.utils.base import logm
from pyriemann.estimation import Covariances
from pyriemann.tangentspace import TangentSpace

from sklearn.preprocessing import LabelBinarizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.svm.classes import LinearSVC as SVM
from sklearn.cross_decomposition import CCA
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.cross_decomposition import PLSCanonical
from sklearn.naive_bayes import MultinomialNB as NB
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import hinge_loss, log_loss, r2_score, mean_squared_error
from sklearn.linear_model import LassoCV, BayesianRidge, LinearRegression
from sklearn.linear_model import LogisticRegression as LR

class LogVariance(BaseEstimator, TransformerMixin):

    def fit(self, X, y):
        """fit."""
        return self

    def transform(self, X):
        """transform"""
        assert X.ndim == 3
        return np.log(np.var(X, -1))


class FM(BaseEstimator, TransformerMixin):

    def __init__(self, freq=128):
        '''instantaneous frequencies require a sampling frequency to be properly
        scaled,
        which is helpful for some algorithms. This assumes 128 if not told
        otherwise.

        '''
        self.freq = freq

    def fit(self, X, y):
        """fit."""
        return self

    def transform(self, X):
        """transform. """
        xphase = np.unwrap(np.angle(signal.hilbert(X, axis=-1)))
        return np.median(self.freq * np.diff(xphase, axis=-1) / (2 * np.pi),
                         axis=-1)


class Feat_convertor(BaseEstimator, TransformerMixin):

    def __init__(self, feat=['IA', 'IF']):
        '''instantaneous frequencies require a sampling frequency to be properly
        scaled,
        which is helpful for some algorithms. This assumes 128 if not told
        otherwise.

        '''
        self.feat = feat

    def fit(self, X, y):
        """fit."""
        return self

    def transform(self, X):
        """transform. """

        exp_nr, elec_nr, t_len = X.shape
        X_n = np.array([], dtype=np.float64).reshape(exp_nr, 0, t_len - 1)
        for i in range(len(self.feat)):
            X_n = np.concatenate((X_n, self._base_tf(X, self.feat[i])), axis=1)

        return X_n

    def _base_tf(self, X, method):

        # Load metadata file
        with open('temp_metadata.yml') as infile:
            metadata = yaml.load(infile)
        self.fs = metadata['info']['sfreq']
        # Load finish & Delete buffer metadata file
        anl_sig = signal.hilbert(X, axis=-1)
        IP = np.unwrap(np.angle(anl_sig))
        all_feat = {'IA': np.abs(anl_sig),
                    'IF': self.fs * np.diff(IP, axis=-1) / (2.0 * np.pi),
                    'IP': IP,
                    'RT': X,
                    'Analytic': anl_sig,
                    'RE': np.real(anl_sig),
                    'IM': np.imag(anl_sig)}

        if method is 'IF':
            return all_feat[method]
        else:
            return all_feat[method][:, :, 1:]

    #  def get_freq():


class TSSF(BaseEstimator, TransformerMixin):

    """ Tangent Space Spatial Filter framework
    

    Parameters
    ----------
    clf_str : 'LR' | 'LDA' | 'SVM', default 'SVM'
        Linear classifier on the tangent space (i.e., the first classifer in [1]).
        'LR': L1 regularized linear regressor (LASSO).
        'LDA': Fisher Linear Discriminant Analysis classifier.
        'SVM': L2 regularized Support Vector Machine using grid search to find best coef. 
    func : 'clf' | 'filter' | 'pattern', default 'clf'
        'clf': To use the classification function of TSSF (incl. both One-step and Two-step classification [1])
        'filter': To plot the derived spatial filters
        'pattern': To plot the associated spatial patterns of TSSF
    n_components: None | int, default None
        Number of used filters components.
        If n_components is not None, a desired number of TSSF components will be adopted.
        Otherwise, defaults to n_channels
    comp_order: None | ndarray, shape (n_components, 1), default None
        If comp_order is not None, an external specified order of components will be adopted.
        Otherwise, the first n_components TSSF will be selected by default.
    decomp: 'ED' | 'GED', default 'GED'
        which kind of decomposition do you want to use to generate the filters
    cov_reg : string, default 'scm'
        Covariance estimator on the sklearn toolbox.
        Other options please refer to sklearn.covariance.
        !!! Please carefully choose diagonal-loading based estimator (Sec. V.E.1 of [1]).
    logvar : bool, default True
        To use log-variance features, i.e., Log-var in Table III.1 of [1], please set to True
        To use logarithm-covariance features, i.e., Diag. log-cov or Log-cov in Table III.1 of [1], please set to False
    ts_metric : string, default 'riemann'
        Riemannian metric for computing the manifold mean. Defaults to 'riemann' (AIRM).
        Other options please refer to pyriemann.mean_covariance()

    Attributes
    ----------
    ts : object, 
        Fitted tangent space for data with full dimensionality
    ts_proj : object, 
        Fitted tangent space for the filtered data (i.e., with reduced dimensionality)
    filters_ :  ndarray, shape (n_channels, n_components)
        If fit, the TSSF components used to decompose the data, else None.
    patterns_ : ndarray, shape (n_channels, n_components)
        If fit, the TSSF patterns used to restore M/EEG signals, else None.
    beta : ndarray, shape (n_components, )
        Coefficient for one-step classification

    References
    ----------

    [1] J. Xu, M. Grosse-Wentrup, and V. Jayaram. Tangent space spatial filters for interpretable and
       efficient Riemannian classification. In: (2019). arXiv: 1909.10567.

    [2] Haufe, S., Meinecke, F., Görgen, K., Dähne, S., Haynes, J. D., Blankertz, B., & Bießmann, F. (2014). 
       On the interpretation of weight vectors of linear models in multivariate neuroimaging.
       Neuroimage, 87, 96-110.
    """

    def __init__(self, clf_str='SVM', func='clf', n_components=None, comp_order=None, 
                 decomp='GED', cov_reg='scm', logvar=True, ts_metric='riemann'):

        self.clf_str = clf_str
        self.func = func
        self.n_components = n_components
        self.comp_order = comp_order
        self.decomp = decomp
        self.cov_reg = cov_reg
        self.logvar = logvar
        self.ts_metric = ts_metric

        self.ts = TangentSpace(metric=ts_metric)
        self.cov_clf = Covariances(estimator=cov_reg)

        self.best_clf = None


    def filter_generator(self, W, Cmean):
        if self.decomp == "ED":
            d, V = linalg.eigh(W)
        elif self.decomp == "GED":
            d, V = linalg.eigh(W, Cmean)
        else:
            raise ValueError("Wrong decomposition! Either ED or GED")

        # Ordering based on log-eigenvalues of GED
        inds = np.argsort(np.abs(np.log(d)))[::-1]

        return V[:, inds], d[inds]

    def TS_classification(self, X, y):
        if self.clf_str == 'LR':
            self.clf_ = LR(penalty='l1')
        elif self.clf_str == 'LDA':
            self.clf_ = LDA()
        elif self.clf_str == 'SVM':
            parameters = {'C': np.logspace(-2, 2, 10)}
            self.clf_ = GridSearchCV(SVC(kernel='linear'), parameters)
        else:
            raise ValueError("Wrong classifier! The supported "
                             "classifiers are: LR(), LDA(), SVM() ")

        # Extract the weight vectors on the tangent space
        # and then projected them onto Riemannian manifold
        if isinstance(self.clf_, GridSearchCV):
            all_clfs = self.clf_.fit(X, y)
            self.best_clf = all_clfs.best_estimator_
            ts_coef = self.best_clf.coef_
        else:
            self.clf_.fit(X, y)
            self.best_clf = self.clf_
        ts_coef = self.best_clf.coef_
        if hasattr(self.best_clf, 'intercept_'):
            self.bias = self.best_clf.intercept_

        self.y_ts_true = ts_coef.dot(X.T)
        #  The reshape function is for the compatibility with Pyriemann pkg.
        cov_mat_coef = self.ts.inverse_transform(np.reshape(ts_coef, [1, -1]))

        return ts_coef, cov_mat_coef[0]

    def fit(self, X, y):
        assert len(np.unique(y)) == 2, "Only works with binary classification"
        self.cov_all = self.cov_clf.transform(X)
        X_ = self.ts.fit_transform(self.cov_all, y)
        cov_mat_mean_ = self.ts.reference_

        # --------------- Classifying on the TS --------------------
        self.w_, self.C_w = self.TS_classification(X_, y)

        # --------------- Extract SF from classifier --------------------
        eigen_vectors, ori_eig = self.filter_generator(self.C_w, cov_mat_mean_)

        # ---------------------- Selecting the SF -------------------------
        #  Select filter components based on given order or the first K comp.
        if self.n_components is not None:
            if self.comp_order is not None:
                filters_ = eigen_vectors[:, self.comp_order]
            else:
                filters_ = eigen_vectors[:, :self.n_components]
        else:
            filters_ = eigen_vectors

        # ---------------------- Applying the SF -------------------------
        if self.func == 'clf':
            self.coef_ = filters_.T

            # Find the new reference point on the low-dim TS
            from pyriemann.tangentspace import TangentSpace as ts_proj
            X_fil = np.asarray([np.dot(self.coef_, epoch) for epoch in X])
            X_cov = self.cov_clf.transform(X_fil)
            self.ts_proj = ts_proj(metric=self.ts_metric).fit(X_cov)

        elif self.func == 'pattern':
            if self.n_components is None:
                #  Simplest  way to derive patterns but requires squire size
                patterns_ = linalg.pinv2(filters_)
            else:
                #  Derive patterns for SF without full rank [1]
                sigma_X = cov_mat_mean_
                sigma_S = np.dot(filters_.T, np.dot(sigma_X, filters_))
                patterns_ = np.dot(sigma_X, np.dot(filters_, linalg.pinv2(sigma_S)))

            self.patterns_ = patterns_

        elif self.func == 'filter':
            self.filters_ = filters_
        else:
            raise ValueError("Valid string for func is either 'filter' or 'pattern'"
                             ", for classification please use 'clf'.")

        self.reg_clf = clone(self.best_clf).fit(X_, y)

        self.ori_eig = ori_eig
        self.beta = np.log(ori_eig[:self.n_components])

        return self

    def transform(self, X):
        if self.func == 'clf':
            X_fil = np.asarray([np.dot(self.coef_, epoch) for epoch in X])
            X_cov = self.cov_clf.transform(X_fil)
            if not self.logvar:
                X_ts = self.ts_proj.transform(X_cov)
            else:
                X_ts = np.asarray([np.log(np.diag(x)) for x in X_cov])
            return X_ts
        elif self.func == 'pattern':
            data_re = {'matrix': self.patterns_, 'data': X}
            return data_re
        elif self.func == 'filter':
            data_re = {'matrix': self.filters_, 'data': X}
            return data_re
        else:
            raise ValueError("Valid string for func is either 'filter' or 'pattern'"
                             ", for classification please use 'clf'.")

    def decision_function(self, X):
        X_filt = np.asarray([np.dot(self.coef_, epoch) for epoch in X])
        if not self.logvar:
            X_ts = np.asarray([np.diag(logm(
                self.cov_clf.transform(x[None, ...])[0])) for x in X_filt])
        else:
            X_ts = np.asarray([np.log(np.var(x, axis=1)) for x in X_filt])
        return X_ts.dot(self.beta)


class TSSF_pattern(BaseEstimator, TransformerMixin):

    def __init__(self, clf_str, n_components, save_path=None, save_type='png',
                 channels=None):
        if clf_str is None:
            raise ValueError("clf_str is compulsory input variable, "
                             "keep same with previous clf_str")
        if n_components is None:
            raise ValueError("n_components is compulsory input variable, "
                             "keep same with previous n_components")
        self.n_components = n_components
        self.clf_str = clf_str

        if save_path is None:
            self.save_path = 'figure/SF/'
            print("Figures will be save into current scirpt's folder.")
        else:
            self.save_path = save_path
            if not os.path.exists(save_path):
                os.mkdir(save_path)
        self.save_type = save_type

        self.channels = channels

    def fit(self, X, y):
        self.y = y
        with open('temp_metadata.yml') as infile:
            metadata = yaml.load(infile)
        info = metadata['info']
        # os.remove('temp_metadata.yml')
        # Load finish & Delete buffer metadata file

        if self.channels is None:
            self.channels = info['ch_names']

        chn_marker = []
        for i in range(len(info['chs'])):
            if info['chs'][i]['kind'] is 2 and info['ch_names'][i] in self.channels:
                chn_marker.append(i)

        info_plot = copy.deepcopy(info)
        info_plot['chs'] = [info['chs'][i] for i in chn_marker]
        info_plot['ch_names'] = [info['ch_names'][i] for i in chn_marker]
        info_plot['nchan'] = len(chn_marker)
        info_plot['sfreq'] = 1.
        # create an evoked
        patterns = EvokedArray(X['matrix'], info_plot, tmin=0)
        # the call plot_topomap
        """
            fig = patterns.plot_topomap(
            times=self.n_components, ch_type=None, layout=None,
            vmin=None, vmax=None, cmap='RdBu_r', colorbar=True, res=64,
            cbar_fmt='%3.1f', sensors=True,
            scalings=1, units='Value', time_unit='s',
            time_format=self.clf_str + '%01d', size=1, show_names=False,
            title=None, mask_params=None, mask=None, outlines='head',
            contours=6, image_interp='bilinear', show=False,
            average=None, head_pos=None)
        """
        fig_name = self.save_path + self.clf_str + '_comp' + str(
            len(self.n_components)) + '_'
        cnt = 0
        while os.path.exists(fig_name + str(cnt) + '.' + self.save_type) is True:
                cnt += 1
        if self.save_type is not 'yml':
            fig.savefig(fig_name + str(cnt) + '.' + self.save_type)
        else:
            with open(fig_name + str(cnt) + '.yml', 'w') as infile:
                yaml.dump(patterns, infile, default_flow_style=False)
        return self

    def transform(self, X):
        return X

    def decision_function(self, X):
        return np.ones(X['data'].shape[0])

class ExtendedSSVEPSignal(BaseEstimator, TransformerMixin):
    """Prepare FilterBank SSVEP EEG signal for estimating extended covariances

    Riemannian approaches on SSVEP rely on extended covariances matrices, where
    the filtered signals are contenated to estimate a large covariance matrice.

    FilterBank SSVEP EEG are of shape (n_trials, n_channels, n_times, n_freqs)
    and should be convert in (n_trials, n_channels*n_freqs, n_times) to
    estimate covariance matrices of (n_channels*n_freqs,  n_channels*n_freqs).
    """
    def __init__(self):
        """Empty init for ExtendedSSVEPSignal"""
        pass

    def fit(self, X, y):
        """No need to fit for ExtendedSSVEPSignal"""
        return self

    def transform(self, X):
        """Transpose and reshape EEG for extended covmat estimation
        """
        out = X.transpose((0, 3, 1, 2))
        n_trials, n_freqs, n_channels, n_times = out.shape
        out = out.reshape((n_trials, n_channels * n_freqs, n_times))
        return out
