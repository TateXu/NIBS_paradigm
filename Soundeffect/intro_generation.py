from jxu.basiccmd.tts import *
loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/q_a_40Hz/'
# bash: google_credential_act

file_name = '1_first_40Hz.mp3'
ssml='<speak>In this block, you will hear German sentences with a missing word censored by forty Hertz noise, which sounds like this. </speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')


file_name = '1_second_40Hz.mp3'
ssml='<speak>And in each trial, the German sentence will be played after a reminding sound like this. </speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')



file_name = '2.mp3'
ssml='<speak>You are expected to fill in this sentence by speaking out your answer after hearing an increasing tonal beeping sound like this. </speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')



file_name = '3.mp3'
ssml='<speak>Afterward, you should speak out your answer after hearing an increasing tonal beeping sound like this.</speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')


file_name = '4.mp3'
ssml='<speak>A decreasing tonal beeping sound indicates this trial is finished, which sounds like this.</speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')




from jxu.audio.audiosignal import *
mp3_to_wav('1_first_40Hz')
mp3_to_wav('1_second_40Hz')
mp3_to_wav('2')
mp3_to_wav('3')
mp3_to_wav('4')

infiles=['1_first_40Hz.wav','40Hz_new.wav', '1_second_40Hz.wav', 'reminder.wav', '2.wav',  'C3A_C4A_tone_decrease_1s_new.wav', '4.wav', 'C4A_C3A_tone_decrease_1s_new.wav','5_new.wav']
outfile='q_a_update_assr.wav'
wav_concat(infiles, outfile)

mp3_to_wav('1_de')
infiles=['1_de.wav', 'C3A_C4A_tone_decrease_1s.wav', '2.wav', 'C4A_C3A_tone_decrease_1s.wav','3.wav']
outfile='cali_de.wav'



#NEW MATERIALS
General:

"<speak>Now, if you are ready to start this block, please press space key to continue.</speak>"

"<speak>This block is finished. Please have some rest and ask for the experimenter for some beverage or snack. If you would like to continue the experiment, please press space key.</speak>"

"<speak>This experiment is finished. Please follow the instructions of the experimenter. Thanks for your participation.</speak>"

Calibration:

from jxu.visualization.audiosignal import beep_generator
beep_generator('A_tone_1s.wav')


'<speak>In this block, each trial will start with a melodious beep sound, which is like this.</speak>'
'<speak>Within each trial, please read out the displayed German sentence after hearing a beep sound with increasing pitch, which is like this.</speak>'
'<speak>This trial will finish after the beep sound with decreasing pitch, which is like this. </speak>'


file_name = '1_de.mp3'


loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')




RS:



RS_intro_text_str = '1. In this block, please keep seated and relaxed.\n' + \
    '2. You will be asked to either open or close eyes in each trial.\n' + \
    '3. A beep sound with decreasing pitch will indicate this trial is finished.'


'<speak>In this block, please keep seated and relaxed.</speak>'
'<speak>You will be asked to either open or close eyes in each trial.</speak>'
'<speak>A beep sound with decreasing pitch will indicate this trial is finished, which is like this.</speak>'



'<speak>Now, please open your eyes and keep relaxed. And blinking eyes is allowed.</speak>'
'<speak>Now, please close your eyes and keep relaxed.</speak>'



file_name = '2.mp3'

loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/resting_state/'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')


mp3_to_wav('1_close')
infiles=['1_close.wav', 'C4A_C3A_tone_decrease_1s.wav', '2.wav']
outfile='rs_close.wav'
wav_concat(infiles, outfile)




Q_A:

'<speak>In this block, each trial will start with a melodious beep sound, which is like this.</speak>'
'<speak>Within each trial, you will first hear a German sentence with a missing word censored by a forty Hertz noise. Subsequently, you should fill in the blank with speaking out your answer after hearing a beep sound with increasing pitch, which is like this.</speak>'
'<speak>Each trial will finish after playing a beep sound with decreasing pitch, which is like this. </speak>'


'<speak>In this block, you will hear one German sentence with a missing word in every trial and you are expected to fill this sentence. These sentences will be played after a flat tonal beeping sound like this. </speak>'
'<speak>After hearing the sentence, you should speak out your answer after hearing an increasing tonal beeping sound like this.</speak>'
'<speak>A decreasing tonal beeping sound indicates this trial is finished, which is like this.</speak>'


loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/q_a/'

file_name = '1_first_40Hz.mp3'
ssml='<speak>In this block, you will hear German sentences with a missing word censored by forty Hertz noise, which sounds like this. </speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')




"""
old demo before 20200304
Calibration:

from jxu.visualization.audiosignal import beep_generator
beep_generator('A_tone_1s.wav')
'<speak>Please read out the displayed German sentence after hearing a beeping sound with increasing pitch.</speak>'

'<speak>And a decreasing tonal beeping sound indicates the recording is finished, which is like this.</speak>'

'<speak>You will have ten seconds of preparation time. Now, please look at the sentences on the screen.</speak>'


file_name = '1_de.mp3'
ssml='<speak>In this block, we will display several sentences written in German on the screen, and please read out them loudly after hearing an increasing tonal beeping sound like this.</speak>'

loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')

mp3_to_wav('1_de')
infiles=['1_de.wav', 'C3A_C4A_tone_decrease_1s.wav', '2.wav', 'C4A_C3A_tone_decrease_1s.wav','3.wav']
outfile='cali_de.wav'


RS:
'<speak>In this block, please remain seated and keep relaxed while opening your eyes. A decreasing tonal beeping sound will indicate this block is finished, which sounds like this.</speak>'

"<speak>Now, let\'s start</speak>"

'In this block, please remain seated and keep relaxed while opening your eyes. A decreasing tonal beeping sound will indicate this block is finished, which sounds like this.'

file_name = '2.mp3'
ssml="<speak>Now, let\'s start</speak>"
loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/resting_state/'

google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')


mp3_to_wav('1_close')
infiles=['1_close.wav', 'C4A_C3A_tone_decrease_1s.wav', '2.wav']
outfile='rs_close.wav'
wav_concat(infiles, outfile)

Q_A:
'<speak>In this block, you will hear one German sentence with a missing word in every trial and you are expected to fill this sentence. These sentences will be played after a flat tonal beeping sound like this. </speak>'
'<speak>After hearing the sentence, you should speak out your answer after hearing an increasing tonal beeping sound like this.</speak>'
'<speak>A decreasing tonal beeping sound indicates this trial is finished, which is like this.</speak>'


loc='/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/q_a/'

file_name = '1_first_40Hz.mp3'
ssml='<speak>In this block, you will hear German sentences with a missing word censored by forty Hertz noise, which sounds like this. </speak>'
google_text_to_speech(ssml_string=ssml, audio_location=loc+file_name, speed=1.0, pitch=0.0, lang='en-US')


"""