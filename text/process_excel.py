import pandas as pd 
import re


filename = 'all_question_anita_3'  # all_question_anita_3_1

all_df = pd.read_excel(filename + '.xlsx')
all_df['complete_sen'] = all_df.apply(lambda x: re.sub(r'(?is)' + '\[MASK\]', x.word, x.beeped_sen_content), axis=1)

unique_df = all_df.drop_duplicates(subset='complete_sen', keep='first')
col_name = ['sentence', 'verb', 'noun']
sen_list = unique_df.complete_sen

restart = None
if restart is not None:
    prev_df = pd.read_pickle(filename + '_' + str(restart) + '.pkl') 


df_list = []
for id_sen, sen_content in enumerate(sen_list):
    if restart is not None:
        if id_sen <= restart:
            continue
    print('---------------------------------------------------')
    print('-----------------{0}/{1}---------------------------'.format(str(id_sen + 1), str(len(sen_list))))
    print('---------------------------------------------------')

    print('Sentence:\n' + sen_content)
    print('\nSuggested answer:\n' + ' '.join(all_df.loc[all_df['complete_sen']==sen_content ].word.values))

    sen_flag = input('\nSentence: 1. Accept, 2. Add "." 3. Rewrite 4. Skip \n')
    if sen_flag == '1':
        sentence = sen_content
    elif sen_flag == '2':
        sentence = sen_content + '.'
    elif sen_flag == '3':
        sentence = input('\nPlease input the rewritten sentences: \n')
    elif sen_flag == '4':
        continue

    verb = input('\nAns-VERB: 1. no, 2. yes \n')
    try: 
        verb_list = [int(verb)]
    except:
        import pdb 
        pdb.set_trace()
        verb = input('\n!!!!! VERBS:  Ans-VERB: 1. no, 2. yes \n')
        verb_list = [int(verb)]

    noun = input('\nAns-NOUN: string with space \n')
    noun_list = noun.split()

    data = {'sentence': [sentence], 'verb': [int(verb)-1], 'noun': [noun_list]}
    df_list.append(pd.DataFrame(data))

    if id_sen % 10 == 0:
        sen_df = pd.concat(df_list, ignore_index=True)
        sen_df.to_pickle(filename + '_' + str(id_sen) + '.pkl')

sen_df = pd.concat(df_list, ignore_index=True)
import pdb 
pdb.set_trace()
if restart is not None:
    final_df = pd.concat([prev_df, sen_df], ignore_index=True)
else:
    final_df = sen_df.copy()

final_df.to_pickle(filename + '.pkl')
