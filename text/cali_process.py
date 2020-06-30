#========================================
# Author     : Jiachen Xu
# Blog       : www.jiachenxu.net
# Time       : 2020-06-30 11:32:29
# Name       : cali_process.py
# Version    : V1.0
# Description: .
#========================================

import pickle
import pandas as pd

all_excel = pd.read_excel('cali_read.xlsx')


for nr_subj in range(11):

    shuffle_df = all_excel.copy().apply(lambda x: x.sample(frac=1).values)
    for nr_ses in range(4):
        with open('../minimal_expfile/cali_info/S{0}_Session{1}_cali.pkl'.format(str(nr_subj).zfill(2), str(nr_ses).zfill(1)), 'wb') as f:
            pickle.dump(shuffle_df.iloc[nr_ses*20: nr_ses*20 + 20], f)
