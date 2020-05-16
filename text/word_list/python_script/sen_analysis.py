import pickle 
import spacy
import re
import pdb
import numpy as np


fileroot = '/home/jxu/File/Experiment/NIBS/Sync/NIBS_paradigm/text/'
with open(fileroot + 'word_list/A1_word.pkl', 'rb') as a1:
    A1_list = pickle.load(a1)

with open(fileroot + 'word_list/A2_word.pkl', 'rb') as a2:
    A2_list = pickle.load(a2)

with open(fileroot + 'word_list/B1_word.pkl', 'rb') as b1:
    B1_list = pickle.load(b1)
with open(fileroot + 'word_list/general_vocab.pkl', 'rb') as g:
    general_list = pickle.load(g)




# A2_only = set(A2_list) - set(A1_list).intersection(set(A2_list))



with open(fileroot + 'all_question_anita_3.pkl', 'rb') as q:
    question = pickle.load(q)
nlp = spacy.load("de_core_news_md")

sen = question.sentence.values
single_sen = sen[0]


doc = nlp(single_sen)
sen_str = single_sen
sen_tag = [token.pos_ for token in doc]
sen_str_list = [token.text for token in doc]

# https://spacy.io/api/annotation#pos-tagging
check = ['VERB', 'NOUN', 'ADJ', 'ADV', 'ADP','INTJ']
uncheck = ['PUNCT', 'ADP', 'AUX','DET','PROPN','PRON','NUM', 'CONJ', 'CCONJ', 'SCONJ','PART','SYM']

sen_level = []
for token in doc:
    if token.pos_ not in check:
        continue
    basic_form = token.lemma_

    a1_flag = True if basic_form in A1_list else False
    a2_flag = True if basic_form in A2_list else False
    b1_flag = True if basic_form in B1_list else False
    general_flag = True if basic_form in general_list else False


    if np.any([a1_flag, a2_flag, b1_flag, general_flag]):
        continue
    else:
        sen_level.append(basic_form)

pdb.set_trace()