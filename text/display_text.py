

'       Welcome for participating the experiment:  \n\n' + \
'       Personalized non-invasive brain stimulation  \n' + \
'              for second language learning          \n' + \
'                                                    \n' + \
'       - Task 1: Read Out                           \n' + \
'       - Task 2: Keepling Relax                     \n' + \
'       - Task 3: Question & Answer                  \n'



Cali_de_pre_intro_text_str = '1. In this block, each trial will start with a melodious beep sound. ' + \
    '2. Within each trial, please read out the displayed German sentence after hearing a beep sound with increasing pitch. \n ' + \
    '3. This trial will finish after the beep sound with decreasing pitch.'

Cali_de_pre_rec_text_str = 'Please read out following sentence.' # discard


fade_str_func = lambda x: 'The stimulation is starting now and we will gradually increase the intensity to '  + \
    str(x*2) + 'mA. \n\n Current current intensity is '

fade_in_str = fade_str_func(max_intensity)
fade_cont_str = 'Increase current intensity press i. \n' + \
    'Remain current intensity and start stimulation press space key. \n' + \
    'Decrease current intensity press d \n'

RS_intro_text_str = '1. In this block, please keep seated and relaxed.\n' + \
    '2. You will be asked to either open or close eyes in each trial.\n' + \
    '3. A beep sound with decreasing pitch will indicate this trial is finished.'


RS_rec_text_str = 'Please keep relaxed and open your eyes.\nBlinking is allowed.'

QA_intro_text_str = '1. You will hear one German sentence with a censored missing word in every trial and ' + \
    'you are expected to fill in this sentence.\n' + \
    '2. These sentences will be played after a flat tonal beeping.\n' + \
    '3. You should speak out your answer after hearing an increasing tonal beeping.\n' + \
    '4. A decreasing tonal beeping sound indicates this trial is finished.'

QA_rec_text_str = 'Listening to the question and speaking out your answer!'
