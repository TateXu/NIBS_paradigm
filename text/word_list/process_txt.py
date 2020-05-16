import re
import pickle

filename = 'B1_word'

with open(filename + '.txt', 'r') as f:
    ori_list = f.read().splitlines()


valid_list = []
for word in ori_list:
    if word == '':
        continue
    no_par_word = re.sub(r'\([^()]*\)', '', word)
    """
    if ',' in word:
        to_check = no_par_word.split(',')
    elif '/' in word:
        to_check = no_par_word.split('/')
    elif ':' in word:
        to_check = no_par_word.split(':')
    else:
        to_check = [no_par_word]   # if [] --> then only Noun will be kept
    """
    # to_check = re.split(r'[;,/,!,:]\s*', no_par_word)
    

    to_check = re.split(';|,|:|!|/|…|→|\n',no_par_word)
    for single_word in to_check:
        single_space = ' '.join(single_word.split())
        if '-' in single_space:
            continue
        if len(single_space) <= 1:
            continue
        all_flag = []
        for single_chac in single_space:
            all_flag.append((single_chac.isalnum()) or (single_chac ==' '))
        if all(all_flag):
            valid_list.append(single_space) 


with open(filename + '.pkl', 'wb') as fw:
    pickle.dump(valid_list, fw)

import pdb 
pdb.set_trace()



























