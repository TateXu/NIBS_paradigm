
import pandas as pd
import numpy as np


all_beep_df = pd.read_pickle('../audio_data/all_unshattered_beep_df.pkl')


all_last_df = all_beep_df.loc[all_beep_df.SENTENCE_INFO.last_word_flag==True]
all_mid_df = all_beep_df.loc[all_beep_df.SENTENCE_INFO.last_word_flag==False]

last_pi = np.asarray(all_last_df.SENTENCE_INFO.permanent_index.values)
mid_pi = np.asarray(all_mid_df.SENTENCE_INFO.permanent_index.values) 



for nr_subj in range(11):
    drop_list = [('EXP_INFO', 'S{0}'.format(str(i_subj).zfill(2))) for i_subj in range(11) if i_subj != nr_subj]
    ind = np.arange(400)
    np.random.shuffle(ind)
    ind_shape = ind.reshape([16, -1])
    subj_df_list = []
    for nr_ses in range(4):
        with_ses = []
        ses_df_list = []
        for nr_block in range(4):
            select_ind = ind_shape[nr_ses*4 + nr_block]
            within_block = np.concatenate((last_pi[select_ind], mid_pi[select_ind]))
            np.random.shuffle(within_block)
            with_ses.append(within_block)
            
            exp_info = ['Ses_{0}, Block_{1}, Q_ind_{2}'.format(nr_ses, nr_block, i) for i in range(50)]
            all_beep_df.loc[within_block - 1, ('EXP_INFO', 'S{0}'.format(str(nr_subj).zfill(2)))] = exp_info

            ses_df_list.append(all_beep_df.copy().iloc[within_block - 1 ])
        ses_df = pd.concat(ses_df_list, ignore_index=True)
        ses_df.drop(columns=drop_list, inplace=True)
        ses_df.to_pickle('qa_info/S{0}_Session{1}_unshattered_beep_df.pkl'.format(str(nr_subj).zfill(2), str(nr_ses)))

        subj_df_list.append(ses_df)
        del ses_df
    subj_df = pd.concat(subj_df_list, ignore_index=True)
    subj_df.sort_values(('SENTENCE_INFO', 'permanent_index'), ascending=True, inplace=True)
    subj_df.to_pickle('qa_info/S{0}_unshattered_beep_df.pkl'.format(str(nr_subj).zfill(2)))    
    del subj_df
all_beep_df.to_pickle('qa_info/all_unshattered_beep_df_randomized.pkl')     
import pdb 
pdb.set_trace()