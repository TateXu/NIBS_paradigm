﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
#============================================================================
# Code: NIBS_Paradigm
# Author: Jiachen XU <jiachen.xu.94@gmail.com>
#
# Last Update: 2020-03-05
#============================================================================
 
from __future__ import absolute_import, division
import pdb
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import pdb
# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler
import sounddevice as sd
from scipy.io.wavfile import write

from nibs_func import *
from jxu.hardware.signal import SignalGenerator as SG
import time
import logging as jxu_logging
import random

jxu_logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s  %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S +0000',
                        filename='/home/jxu/File/Experiment/NIBS/Sync/NIBS_paradigm/minimal_expfile/main.log',
                        filemode='w')

# -----------------------------------------------------------------------------------
# ------------------------- Setting: Parameter --------------------------------------
# -----------------------------------------------------------------------------------

######## Psychopy basic setting ########
endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
continue_str = '          Press [space] key to continue.'
font_type = 'Airal'



instruction_pos = [0.5, 0.1]
instruction_annot_pos = [0.5, -0.4]
title_pos = [0.5, 0.4]
qa_inrto_title_pos = [0.5, 0.5]
text_pos = [0.5, 0]
annot_pos = [0.5, 0.0]
audio_root = '/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/'
question_root = '/home/jxu/File/Data/NIBS/Stage_one/Audio/Database/'

######## Paradigm setting ########
n_run = 4
n_block = 2
n_trial = 20  # 10 mins
n_cali_trial = 10

n_question = n_run * n_block * n_trial + n_cali_trial * 2

fs = 44100  # Sample rate of audio
n_rec_chn = 1

stim_run = [1, 2]  # In which run, the stimulation is applied.
init_intensity, min_intensity, max_intensity = 0.002, 0.005, 0.5
intensity_goal = [0, max_intensity, max_intensity, 0]  # i.e., of each session 
stim_freq = 10
fade_in_auto_incre = 6
n_step_fade_stim = 5

step_intensity = max_intensity / n_step_fade_stim

input_intensity = init_intensity
output_intensity = init_intensity

######## Component switch ########
init_flag = True  # NEVER TURN OFF THIS FLAG!!! For initializing the components


external_question_flag = 1
question_cnt = -1
word_type = 'VERB'

fade_in_out_show = False
always_dislpay = True

comp_gap = 0.4
instruction_cont_start, instruction_cont_dur = 20, None

cali_intro_start, cali_intro_dur, cali_intro_cont_dur = 0, 30, None
cali_intro_cont_start = cali_intro_start + cali_intro_dur + comp_gap

cali_hint_start, cali_hint_dur, cali_q_dur, cali_a_beep_s_dur, cali_rec_dur, cali_a_beep_e_dur, cali_break_dur = 0, 2, 5, 1, 17, 1, 2
cali_q_start = cali_hint_start + cali_hint_dur + comp_gap
cali_a_beep_s_start = cali_q_start + cali_q_dur + comp_gap
cali_rec_start = cali_a_beep_s_start + cali_a_beep_s_dur + comp_gap
cali_a_beep_e_start = cali_rec_start + cali_rec_dur + comp_gap
cali_break_start = cali_a_beep_e_start + cali_a_beep_e_dur + comp_gap
cali_text_dur = cali_break_start + cali_break_dur


if always_dislpay:
    cali_q_dur = cali_text_dur - cali_q_start



rs_intro_text_start, rs_intro_text_dur, rs_intro_cont_dur = 0, 180, None
rs_intro_cont_start = rs_intro_text_start + rs_intro_text_dur + comp_gap

rs_rec_text_start, rs_rec_text_dur, rs_rec_beep_e_dur, rs_rec_cont_dur = 0, 10, 1, None
rs_rec_beep_e_start = rs_rec_text_start + rs_rec_text_dur + comp_gap 
rs_rec_cont_start = rs_rec_beep_e_start + rs_rec_beep_e_dur + comp_gap

QA_intro_title_start, QA_intro_title_dur, QA_intro_audio_dur, QA_intro_cont_dur = 0, 40, 40, None
QA_intro_cont_start = QA_intro_title_start + QA_intro_title_dur + comp_gap

QA_hint_start, QA_hint_dur, QA_q_dur, QA_a_beep_s_dur, QA_rec_dur, QA_a_beep_e_dur, QA_break_dur = 0, 2, 14, 1, 8, 1, 2
QA_q_start = QA_hint_start + QA_hint_dur + comp_gap
QA_a_beep_s_start = QA_q_start + QA_q_dur + comp_gap
QA_rec_start = QA_a_beep_s_start + QA_a_beep_s_dur + comp_gap
QA_a_beep_e_start = QA_rec_start + QA_rec_dur + comp_gap
QA_break_start = QA_a_beep_e_start + QA_a_beep_e_dur + comp_gap
QA_text_dur = QA_break_start + QA_break_dur

flexible_qa_rec_start = True
if flexible_qa_rec_start and external_question_flag:
    QA_trial_dur = 30.00
    QA_text_dur = QA_trial_dur
    QA_break_start = QA_text_dur - QA_break_dur
    QA_a_beep_e_start = QA_break_start - QA_a_beep_e_dur - comp_gap


    
trigger_sending(254)   # trigger 254 represents real experiment

# -----------------------------------------------------------------------------------
# ------------------------ Setting: Initialization ----------------------------------
# -----------------------------------------------------------------------------------
if init_flag:

    expInfo, win, frameDur, defaultKeyboard  = exp_init()
    folder_path, filename = path_init(expInfo)

    font_size = (0.06 if not expInfo['Full_screen'] else 0.15)

    Instruction_flag = expInfo['Instruction']
    Cali_de_pre_intro_flag = expInfo['Cali_pre']
    Cali_de_pre_rec_flag = expInfo['Cali_pre']
    fade_in_flag = expInfo['Fade_in_out']
    fade_out_flag = expInfo['Fade_in_out']
    RS_intro_flag = expInfo['Resting_State']
    RS_rec_flag = expInfo['Resting_State']
    QA_intro_flag = expInfo['QA']
    QA_rec_flag = expInfo['QA']
    Pause_flag = expInfo['Pause']
    Cali_de_post_intro_flag = expInfo['Cali_post']
    Cali_de_post_rec_flag = expInfo['Cali_post']
    end_flag = expInfo['End']

    break_cali_pre_trial = (None if expInfo['Breakpoint_Cali_pre_trial'] == 'No' else int(expInfo['Breakpoint_Cali_pre_trial']))
    break_cali_post_trial = (None if expInfo['Breakpoint_Cali_post_trial'] == 'No' else int(expInfo['Breakpoint_Cali_post_trial']))
    break_run = (None if expInfo['Breakpoint_Run'] == 'No' else int(expInfo['Breakpoint_Run']))
    break_rs_block = (None if expInfo['Breakpoint_RS_block'] == 'No' else int(expInfo['Breakpoint_RS_block'])) 
    break_qa_block = (None if expInfo['Breakpoint_QA_block'] == 'No' else int(expInfo['Breakpoint_QA_block']))  
    break_qa_trial = (None if expInfo['Breakpoint_QA_trial'] == 'No' else int(expInfo['Breakpoint_QA_trial'])) 
    

    if external_question_flag:
        pre_load_df = pd.read_pickle('/home/jxu/File/Data/NIBS/Stage_one/Audio/Database/Q_Session_' + str(int(expInfo['session'])) + '_exp_' + str(180) + '.pkl')
        extract_df, question_path, censor_question_start, censor_question_duration, sen_duration, sen_text = extract_qa(
            input_all_df=pre_load_df,
            subject=int(expInfo['participant']),
            session=int(expInfo['session']), word_type=word_type, n_question=n_question, shuffle_flag=True)


    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    instruction_text_str = '     Thank you for participating in the experiment: \n\n' + \
        '     Personalized non-invasive brain stimulation    \n' + \
        '            for second language learning            \n'

    instruction_comp_list = [
        textstim_generator(win=win, name='text', content=instruction_text_str, pos=instruction_pos),
        audio_generator(name='audio', loc=audio_root+'Instruction_main.wav', secs=-1),
        key_resp_generator(name='key_resp'), 
        textstim_generator(win=win, name='cont', content=continue_str, pos=instruction_annot_pos)
        ]
    instruction = routine_init('instruction', instruction_comp_list)
    instruction['time'] = {'text':[0, instruction_cont_dur],
                           'audio':[0, instruction_cont_dur],
                           'key_resp':[instruction_cont_start, instruction_cont_dur],
                           'cont':[instruction_cont_start, instruction_cont_dur]}



    # Initialize components for Routine "Cali_de_pre_intro
    Cali_de_pre_intro_text_str = '  - Task: Read out the displayed German sentence   \n' + \
        '  - Melodious beep sound: Trial start              \n' + \
        '  - Beep sound with increasing pitch: Rec. start   \n' + \
        '  - Beep sound with decreasing pitch: Rec. finish  \n'

    Cali_de_pre_intro_comp_list = [
        textstim_generator(win=win, name='title', content='READ OUT BLOCK (GERMAN)', pos=title_pos),
        textstim_generator(win=win, name='text', content=Cali_de_pre_intro_text_str, pos=text_pos),
        audio_generator(name='audio', loc=audio_root+'calibration/calibration.wav', secs=-1),
        key_resp_generator(name='key_resp'),
        textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
        ]
    Cali_de_pre_intro = routine_init('Cali_de_pre_intro', Cali_de_pre_intro_comp_list)
    Cali_de_pre_intro['time'] = {'title':[cali_intro_start, cali_intro_dur],
                                 'text':[cali_intro_start, cali_intro_dur],
                                 'audio':[cali_intro_start, cali_intro_dur],
                                 'key_resp':[cali_intro_cont_start, cali_intro_cont_dur],
                                 'cont':[cali_intro_cont_start, cali_intro_cont_dur]}

    # Initialize components for Routine "Cali_de_pre_rec"
    Cali_de_pre_rec_text_str = ''  # Please read out following sentence.
    Cali_de_pre_rec_comp_list = [
        textstim_generator(win=win, name='text', content=Cali_de_pre_rec_text_str, pos=title_pos),
        audio_generator(name='beep_hint', loc=audio_root+'calibration/reminder.wav', secs=0.6),
        textstim_generator(win=win, name='question_text', content=Cali_de_pre_rec_text_str, pos=text_pos),
        audio_generator(name='beep_start', loc=audio_root+'calibration/C3A_C4A_tone_decrease_1s_new.wav', secs=1),
        rec_generator(name='recording', sps=fs, loc='./data/', n_rec_chn=n_rec_chn),
        audio_generator(name='beep_end', loc=audio_root+'calibration/C4A_C3A_tone_decrease_1s_new.wav', secs=1),
        textstim_generator(win=win, name='break', content='Short break', pos=instruction_annot_pos)
        ] 

    Cali_de_pre_rec = routine_init('Cali_de_pre_rec', Cali_de_pre_rec_comp_list)
    Cali_de_pre_rec['time'] = {'text':[0, cali_text_dur],
                               'beep_hint':[cali_hint_start, cali_hint_dur],
                               'question_text':[cali_q_start, cali_q_dur],
                               'beep_start':[cali_a_beep_s_start, cali_a_beep_s_dur],
                               'recording':[cali_rec_start, cali_rec_dur],
                               'beep_end':[cali_a_beep_e_start, cali_a_beep_e_dur],
                               'break':[cali_break_start, cali_break_dur]}

    # Initialize components for Routine "fade_in"
    fade_str_func = lambda x: 'The stimulation is starting now and we will gradually increase the intensity to '  + \
        str(x*2) + 'mA. \n\n Current current intensity is '

    fade_in_str = '' #  fade_str_func(max_intensity)
    fade_cont_str = 'Increase current intensity press i. \n' + \
        'Remain current intensity and start stimulation press space key. \n' + \
        'Decrease current intensity press d \n'
    fade_in_list = [
        textstim_generator(win=win, name='text', content=fade_in_str, pos=[0.5, 0.4]),
        key_resp_generator(name='auto_stim')
        ]
    fade_in = routine_init('fade_in', fade_in_list)
    fade_in['time'] = {'text':[0, fade_in_auto_incre], 'auto_stim':[0, fade_in_auto_incre]}
    

    # Initialize components for Routine "RS_intro"

    RS_intro_text_str = ' - Task: Keep seated and relaxed with either      \n' + \
        '             opening or closing eyes                  \n' + \
        ' - Beep sound with decreasing pitch: Block finish \n'

    RS_intro_comp_list = [
        textstim_generator(win=win, name='title', content='REST STATE BLOCK', pos=title_pos),
        textstim_generator(win=win, name='text', content=RS_intro_text_str, pos=text_pos),
        audio_generator(name='audio', loc=audio_root+'resting_state/rs.wav', secs=-1)
        ]
    RS_intro = routine_init('RS_intro', RS_intro_comp_list)
    RS_intro['time'] = {'title':[rs_intro_text_start, rs_intro_text_dur],
                        'text':[rs_intro_text_start, rs_intro_text_dur],
                        'audio':[rs_intro_text_start, rs_intro_text_dur]}

    # Initialize components for Routine "RS_rec"
    RS_rec_text_str = 'Please keep relaxed and open your eyes.\nNote: Blinking is allowed.'
    RS_rec_comp_list = [
        textstim_generator(win=win, name='text', content=RS_rec_text_str, pos=text_pos),
        audio_generator(name='beep_end', loc=audio_root+'resting_state/C4A_C3A_tone_decrease_1s_new.wav', secs=1),
        key_resp_generator(name='key_resp'),
        textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
        ]
    RS_rec = routine_init('RS_rec', RS_rec_comp_list)
    RS_rec['time'] = {'text':[rs_rec_text_start, rs_rec_text_dur],
                      'beep_end': [rs_rec_beep_e_start, rs_rec_beep_e_dur], 
                      'key_resp':[rs_rec_cont_start, rs_rec_cont_dur],
                      'cont':[rs_rec_cont_start, rs_rec_cont_dur]}

    # Initialize components for Routine "QA_intro"
    QA_intro_text_str = ' - Task: Listen to the question& Speak out answer \n' + \
        ' - Melodious beep sound: Trial start              \n' + \
        ' - 40 Hz beep (blank): censored word              \n' + \
        ' - Beep sound with increasing pitch: Rec. start   \n' + \
        ' - Beep sound with decreasing pitch: Rec. finish  \n'
    QA_intro_comp_list = [ 
        textstim_generator(win=win, name='title', content='Q&A BLOCK', pos=qa_inrto_title_pos),
        textstim_generator(win=win, name='text', content=QA_intro_text_str, pos=text_pos),
        audio_generator(name='audio', loc=audio_root+'q_a_40Hz/q_a_update_assr.wav', secs=-1),
        key_resp_generator(name='key_resp'),
        textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
        ]
    QA_intro = routine_init('QA_intro', QA_intro_comp_list)
    QA_intro['time'] = {'title':[QA_intro_title_start, QA_intro_title_dur],
                        'text':[QA_intro_title_start, QA_intro_title_dur],
                        'audio':[QA_intro_title_start, QA_intro_title_dur],
                        'key_resp':[QA_intro_cont_start, QA_intro_cont_dur],
                        'cont':[QA_intro_cont_start, QA_intro_cont_dur]}
    

    # Initialize components for Routine "QA_rec"
    QA_rec_text_str = 'Listen to the question and speak out your answer!'
    QA_rec_comp_list = [
        textstim_generator(win=win, name='text', content=QA_rec_text_str, pos=text_pos),
        audio_generator(name='beep_hint', loc=audio_root+'q_a_40Hz/reminder.wav', secs=0.6),
        audio_generator(name='question', loc=question_root+'old_data/article_0/sentence_0/sentence_0_syn_44100.wav', secs=1),
        audio_generator(name='beep_start', loc=audio_root+'q_a_40Hz/C3A_C4A_tone_decrease_1s_new.wav', secs=1),
        rec_generator(name='recording', sps=fs, loc='./data/', n_rec_chn=n_rec_chn),
        audio_generator(name='beep_end', loc=audio_root+'q_a_40Hz/C4A_C3A_tone_decrease_1s_new.wav', secs=1),
        textstim_generator(win=win, name='break', content='Short break', pos=instruction_annot_pos),
        trigger_generator(win=win, name='censor_word')
        ]
    QA_rec = routine_init('QA_rec', QA_rec_comp_list)
    QA_rec['time'] = {'text':[0, QA_text_dur],
                      'beep_hint':[QA_hint_start, QA_hint_dur],
                      'question':[QA_q_start, QA_q_dur],
                      'beep_start':[QA_a_beep_s_start, QA_a_beep_s_dur],
                      'recording':[QA_rec_start, QA_rec_dur],
                      'beep_end':[QA_a_beep_e_start, QA_a_beep_e_dur],
                      'break':[QA_break_start, QA_break_dur],
                      'censor_word':[0, 0]}

    # Initialize components for Routine "Pause"
    Pause_str = 'Pause: Please have some rest and \n'+ continue_str
    Pause_comp_list = [
        audio_generator(name='audio', loc=audio_root+'block_finish.wav', secs=-1),
        key_resp_generator(name='key_resp'),
        textstim_generator(win=win, name='cont', content=Pause_str, pos=annot_pos)
        ]
    Pause = routine_init('Pause', Pause_comp_list)
    Pause['time'] = {'audio': [0, 12], 'key_resp':[12, None], 'cont':[0, None]}

    # Initialize components for Routine "Cali_de_post_intro"
    Cali_de_post_intro_text_str = '  - Task: Read out the displayed German sentence   \n' + \
        '  - Melodious beep sound: Trial start              \n' + \
        '  - Beep sound with increasing pitch: Rec. start   \n' + \
        '  - Beep sound with decreasing pitch: Rec. finish  \n'

    Cali_de_post_intro_comp_list = [
        textstim_generator(win=win, name='title', content='READ OUT BLOCK (GERMAN)', pos=title_pos),
        textstim_generator(win=win, name='text', content=Cali_de_post_intro_text_str, pos=text_pos),
        audio_generator(name='audio', loc=audio_root+'calibration/calibration.wav', secs=-1),
        key_resp_generator(name='key_resp'),
        textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
        ]
    Cali_de_post_intro = routine_init('Cali_de_post_intro', Cali_de_post_intro_comp_list)
    Cali_de_post_intro['time'] = {'title':[cali_intro_start, cali_intro_dur],
                                  'text':[cali_intro_start, cali_intro_dur],
                                  'audio':[cali_intro_start, cali_intro_dur],
                                  'key_resp':[cali_intro_cont_start, cali_intro_cont_dur],
                                  'cont':[cali_intro_cont_start, cali_intro_cont_dur]}

    # Initialize components for Routine "Cali_de_post_rec"
    Cali_de_post_rec_text_str = ''
    Cali_de_post_rec_comp_list = [
        textstim_generator(win=win, name='text', content=Cali_de_post_rec_text_str, pos=title_pos),
        audio_generator(name='beep_hint', loc=audio_root+'calibration/reminder.wav', secs=0.6),
        textstim_generator(win=win, name='question_text', content=Cali_de_pre_rec_text_str, pos=text_pos),
        audio_generator(name='beep_start', loc=audio_root+'calibration/C3A_C4A_tone_decrease_1s_new.wav', secs=1),
        rec_generator(name='recording', sps=fs, loc='./data/', n_rec_chn=n_rec_chn),
        audio_generator(name='beep_end', loc=audio_root+'calibration/C4A_C3A_tone_decrease_1s_new.wav', secs=1),
        textstim_generator(win=win, name='break', content='Short break', pos=instruction_annot_pos)
        ]

    Cali_de_post_rec = routine_init('Cali_de_post_rec', Cali_de_post_rec_comp_list)
    Cali_de_post_rec['time'] = {'text':[0, cali_text_dur],
                                'beep_hint':[cali_hint_start, cali_hint_dur],
                                'question_text':[cali_q_start, cali_q_dur],
                                'beep_start':[cali_a_beep_s_start, cali_a_beep_s_dur],
                                'recording':[cali_rec_start, cali_rec_dur],
                                'beep_end':[cali_a_beep_e_start, cali_a_beep_e_dur],
                                'break':[cali_break_start, cali_break_dur]}


    # Initialize components for Routine "the_end"
    the_end_comp_list = [
        audio_generator(name='audio', loc=audio_root+'exp_finish.wav', secs=-1),
        textstim_generator(win=win, name='text', content=' This experiment is finished. \nThanks for your participation.', pos=[0.7, 0.0])
        ]
    the_end = routine_init('the_end', the_end_comp_list)
    the_end['time'] = {'audio': [0, 10],  'text':[0, 10]}






    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# -----------------------------------------------------------------------------------
# ------------------------------ Start Exp. -----------------------------------------
# -----------------------------------------------------------------------------------
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expInfo['expName'], version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='nibs_minimal_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

def breakpoint_logger(comp, value, run, block, trial):
    jxu_logging.info('%s %d %s %s %s' %(comp, value, run, block, trial) )
# ---------------------------------------------------
# ----------------- instruction ---------------------
# ---------------------------------------------------




if Instruction_flag:
    print('Log: instruction start')

    breakpoint_logger(comp='Instruction', value=1, run=None, block=None, trial=None)
    # ------Prepare to start Routine "instruction"-------
    # update component parameters for each repeat
    instruction['key_resp'].keys = []
    instruction['key_resp'].rt = []
    # keep track of which components have finished
    win, instruction, instructionComponents, t, frameN, continueRoutine = pre_run_comp(win, instruction)
    trigger_mat = np.zeros((len(instructionComponents) - 1, 2))
    comp_list = np.asarray([*instruction['time'].keys()])
    # trigger_encoding_sending('instruction', input_run=0, input_block=0, intro_rec=0, input_event=0)
    # -------Run Routine "instruction"-------
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            instruction["clock"], win, frameN)

        # *instruction["text"]* updates
        win, instruction['text'], trigger_mat[0] = run_comp(
            win, instruction['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=instruction['time']['text'][0], duration=instruction['time']['text'][1])

        # *instruction["audio"]* updates
        win, instruction['audio'], trigger_mat[1] = run_comp(
            win, instruction['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=instruction['time']['audio'][0], duration=instruction['time']['audio'][1])
        # *instruction['key_resp']* updates
        waitOnFlip=False
        win, instruction['key_resp'], continueRoutine, endExpNow, trigger_mat[2] = run_comp(
            win, instruction['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=instruction['time']['key_resp'][0], duration=instruction['time']['key_resp'][1],
            waitOnFlip=waitOnFlip)   
        
        # *instruction['cont']* updates
        win, instruction['cont'], trigger_mat[3] = run_comp(
            win, instruction['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=instruction['time']['cont'][0], duration=instruction['time']['cont'][1])

        break_flag = False
        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, instructionComponents)

        if trigger_mat.sum(axis=0)[0]:
            pass # trigger_encoding_sending('instruction', input_run=0, input_block=0, intro_rec=0, input_event=trigger_mat)
        if break_flag:
            break
    # trigger_encoding_sending('instruction', input_run=0, input_block=0, intro_rec=0, input_event=2)
    # -------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp = data_writer(thisExp, instruction, 'instruction', ['text', 'cont'])
    print('Log: instruction finish')
    breakpoint_logger(comp='Instruction', value=0, run=None, block=None, trial=None)
    routineTimer.reset()



trigger_sending(0)  # Sending trigger 0 (Pre-Run Intro Start)
time.sleep(0.003)
# ---------------------------------------------------
# -------------- Cali_de_pre_intro ------------------
# ---------------------------------------------------
if Cali_de_pre_intro_flag:
    print('Log: cali_pre_intro start')
    breakpoint_logger(comp='Cali_de_pre_intro', value=1, run=None, block=None, trial=None)
    # ------Prepare to start Routine "Cali_de_pre_intro"-------
    # update component parameters for each repeat
    Cali_de_pre_intro['key_resp'].keys = []
    Cali_de_pre_intro['key_resp'].rt = []
    # keep track of which components have finished
    win, Cali_de_pre_intro, Cali_de_pre_introComponents, t, frameN, continueRoutine = pre_run_comp(win, Cali_de_pre_intro)
    trigger_mat = np.zeros((len(Cali_de_pre_introComponents) - 1, 2))
    comp_list = np.asarray([*Cali_de_pre_intro['time'].keys()])

    Cali_de_pre_intro['audio'].setSound(audio_root+'calibration/calibration.wav',secs=-1, hamming=True)
    # -------Run Routine "Cali_de_pre_intro"-------
    
    trigger_sending(10)  # Sending trigger 0 (Pre-Run Start)
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            Cali_de_pre_intro["clock"], win, frameN)
        # update/draw components on each frame
        
        # *Cali_de_pre_intro["title"]* updates
        win, Cali_de_pre_intro['title'], trigger_mat[0] = run_comp(
            win, Cali_de_pre_intro['title'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_pre_intro['time']['title'][0], duration=Cali_de_pre_intro['time']['title'][1])
        # *Cali_de_pre_intro["title"]* updates
        win, Cali_de_pre_intro['text'], trigger_mat[1] = run_comp(
            win, Cali_de_pre_intro['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_pre_intro['time']['text'][0], duration=Cali_de_pre_intro['time']['text'][1])
        # *Cali_de_pre_intro["audio"]* updates
        win, Cali_de_pre_intro['audio'], trigger_mat[2] = run_comp(
            win, Cali_de_pre_intro['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_pre_intro['time']['audio'][0], duration=Cali_de_pre_intro['time']['audio'][1])

        # *Cali_de_pre_intro['key_resp']* updates
        waitOnFlip=False
        win, Cali_de_pre_intro['key_resp'], continueRoutine, endExpNow, trigger_mat[3] = run_comp(
            win, Cali_de_pre_intro['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_pre_intro['time']['key_resp'][0], duration=Cali_de_pre_intro['time']['key_resp'][1],
            waitOnFlip=waitOnFlip)   
        # *Cali_de_pre_intro['cont']* updates
        win, Cali_de_pre_intro['cont'], trigger_mat[4] = run_comp(
            win, Cali_de_pre_intro['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_pre_intro['time']['cont'][0], duration=Cali_de_pre_intro['time']['cont'][1],
            repeat_per_frame=True, repeat_content=continue_str)
        
        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, Cali_de_pre_introComponents)
        if trigger_mat.sum(axis=0)[0]:
            pass # trigger_encoding_sending('Calibration', input_run=0, input_block=0, intro_rec=0, input_event=trigger_mat)
        if break_flag:
            break

    # -------Ending Routine "Cali_de_pre_intro"-------
    for thisComponent in Cali_de_pre_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    thisExp = data_writer(thisExp, Cali_de_pre_intro, 'Cali_de_pre_intro', ['title', 'text', 'audio', 'cont'])
    trigger_sending(11)  # Sending trigger 0 (Pre-Run Intro End)
    # the Routine "Cali_de_pre_intro" was not non-slip safe, so reset the non-slip timer
    print('Log: cali_pre_intro finish')
    breakpoint_logger(comp='Cali_de_pre_intro', value=0, run=None, block=None, trial=None)
    routineTimer.reset()



# ---------------------------------------------------------------------------
# ------------------------ Start Calibration Trial --------------------------
# ---------------------------------------------------------------------------
# set up handler to look after randomisation of conditions etc

cali_pre_trial = data.TrialHandler(nReps=n_cali_trial, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pre_trial')
thisExp.addLoop(cali_pre_trial)  # add the loop to the experiment
thisCali_pre_trial = cali_pre_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCali_pre_trial.rgb)
if thisCali_pre_trial != None:
    for paramName in thisCali_pre_trial:
        exec('{} = thisCali_pre_trial[paramName]'.format(paramName))

for thisCali_pre_trial in cali_pre_trial:

    if break_cali_pre_trial != None and cali_pre_trial.thisN < break_cali_pre_trial:
        continue
    break_cali_pre_trial = None   # clear the breakpoint

    currentLoop = cali_pre_trial
    # abbreviate parameter names if possible (e.g. rgb = thisCali_pre_trial.rgb)
    if thisCali_pre_trial != None:
        for paramName in thisCali_pre_trial:
            exec('{} = thisCali_pre_trial[paramName]'.format(paramName))
    trigger_sending(12)
    time.sleep(0.003)
    # ---------------------------------------------------
    # --------------- Cali_de_pre_rec -------------------
    # ---------------------------------------------------
    if Cali_de_pre_rec_flag:
        print('Log: cali_pre_rec start: Trial ' + str(cali_pre_trial.thisN))
        breakpoint_logger(comp='Cali_de_pre_rec', value=1, run=None, block=None, trial=cali_pre_trial.thisN)
        # ------Prepare to start Routine "Cali_de_pre_rec"-------
        # ------Prepare to start Routine "QA_rec"-------
        routineTimer.add(30.000000)
        # update component parameters for each repeat

        """
            # update component parameters for each repeat
            ques_start = QA_rec['time']['question'][0]
            if external_question_flag:
                question_cnt += 1
                Cali_de_pre_rec['question_text'].setText(sen_text[question_cnt])
                Cali_de_pre_rec['time']['question'][1] = sen_duration[question_cnt] - 0.016
                if flexible_qa_rec_start:
                    QA_trial_dur = 30.00
                    QA_rec['time']['beep_start'][0] = QA_q_start + sen_duration[question_cnt] + comp_gap
                    QA_rec['time']['recording'][0] = QA_rec['time']['beep_start'][0] + QA_a_beep_s_dur + comp_gap
                    QA_rec['time']['recording'][1] = QA_a_beep_e_start - QA_rec['time']['recording'][0] - comp_gap
            else:
                QA_rec['question'].setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Database/old_data/article_0/sentence_0/sentence_0_syn_44100.wav', secs=-1, hamming=True)
                QA_rec['time']['question'][1] = 5.63 - 0.02
        """

        if external_question_flag:
            question_cnt += 1
            Cali_de_pre_rec['question_text'].setText(sen_text[question_cnt])
        else:
            Cali_de_pre_rec['question_text'].setText('Text ' + str(cali_pre_trial.thisN))

        # update component parameters for each repeat 
        # Cali_de_pre_rec['key_resp'].keys = []
        # Cali_de_pre_rec['key_resp'].rt = []

        # keep track of which components have finished
        win, Cali_de_pre_rec, Cali_de_pre_recComponents, t, frameN, continueRoutine = pre_run_comp(win, Cali_de_pre_rec)
        trigger_mat = np.zeros((len(Cali_de_pre_recComponents) - 1, 2))
        comp_list = np.asarray([*Cali_de_pre_rec['time'].keys()])
        # trigger_encoding_sending('Calibration', input_run=0, input_block=0, intro_rec=1, input_event=0)
        # -------Run Routine "Cali_de_pre_rec"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                Cali_de_pre_rec["clock"], win, frameN)
            
            # *Cali_de_pre_rec["text"]* updates
            win, Cali_de_pre_rec['text'], trigger_mat[0] = run_comp(
                win, Cali_de_pre_rec['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['text'][0], duration=Cali_de_pre_rec['time']['text'][1])
            # *Cali_de_pre_rec["beep_hint"]* updates
            win, Cali_de_pre_rec['beep_hint'], trigger_mat[1] = run_comp(
                win, Cali_de_pre_rec['beep_hint'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['beep_hint'][0], duration=Cali_de_pre_rec['time']['beep_hint'][1])

            # *Cali_de_pre_rec["question_text"]* updates
            win, Cali_de_pre_rec['question_text'], trigger_mat[2] = run_comp(
                win, Cali_de_pre_rec['question_text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['question_text'][0], duration=Cali_de_pre_rec['time']['question_text'][1])

            # *Cali_de_pre_rec["beep_start"]* updates
            win, Cali_de_pre_rec['beep_start'], trigger_mat[3] = run_comp(
                win, Cali_de_pre_rec['beep_start'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['beep_start'][0], duration=Cali_de_pre_rec['time']['beep_start'][1])
            # *Cali_de_pre_rec["recording"]* updates
            win, Cali_de_pre_rec['recording'], trigger_mat[4] = run_comp(
                win, Cali_de_pre_rec['recording'], 'recording', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['recording'][0], duration=Cali_de_pre_rec['time']['recording'][1])
            # *Cali_de_pre_rec["beep_end"]* updates
            win, Cali_de_pre_rec['beep_end'], trigger_mat[5] = run_comp(
                win, Cali_de_pre_rec['beep_end'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['beep_end'][0], duration=Cali_de_pre_rec['time']['beep_end'][1])

            win, Cali_de_pre_rec['break'], trigger_mat[6] = run_comp(
                win, Cali_de_pre_rec['break'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_pre_rec['time']['break'][0], duration=Cali_de_pre_rec['time']['break'][1])

            win, continueRoutine, break_flag = continue_justification(
                win, endExpNow, defaultKeyboard, continueRoutine, Cali_de_pre_recComponents)

            if trigger_mat.sum(axis=0)[0]:
                trigger_encoding_sending('Calibration', input_event=trigger_mat)
            if break_flag:
                break
        # trigger_encoding_sending('Calibration', input_run=0, input_block=0, intro_rec=1, input_event=6)
        # -------Ending Routine "Cali_de_pre_rec"-------
        for thisComponent in Cali_de_pre_recComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        thisExp = data_writer(thisExp, Cali_de_pre_rec, 'Cali_de_pre_rec', ['text', 'beep_hint', 'question_text', 'beep_start', 'beep_end', 'break'])

        # cali_pre_rec_file = folder_path + 'rec_cali_de_pre_' + + ' .wav'
        cali_pre_rec_file = folder_path + 'rec_cali_de_pre_' + 'trial_' + str(cali_pre_trial.thisN).zfill(3)  + '.wav' 
        write(cali_pre_rec_file, fs, Cali_de_pre_rec['recording'].file)  # Save as WAV file 
        print('Recording is saved!' + cali_pre_rec_file)
        # Add the detected time into the PsychoPy data file:
        thisExp.addData('filename', cali_pre_rec_file)
        
        thisExp.nextEntry()
        print('Log: cali_pre_rec finish: Trial' + str(cali_pre_trial.thisN))
        breakpoint_logger(comp='Cali_de_pre_rec', value=0, run=None, block=None, trial=cali_pre_trial.thisN)
        # the Routine "Cali_de_pre_rec" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    time.sleep(0.003)
    trigger_sending(13)
    time.sleep(0.003)



# ---------------------------------------------------
# --------------------- Pause -----------------------
# ---------------------------------------------------
if Pause_flag:
    trigger_sending(60)
    # ------Prepare to start Routine "Pause"-------
    # update component parameters for each repeat
    Pause['key_resp'].keys = []
    Pause['key_resp'].rt = []
    Pause['cont'].setText('Pause: Please have some rest and '+ continue_str)

    # keep track of which components have finished
    win, Pause, PauseComponents, t, frameN, continueRoutine = pre_run_comp(win, Pause)
    # -------Run Routine "Pause"-------
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            Pause["clock"], win, frameN)
        # update/draw components on each frame
        # *Pause['audio']* updates
        win, Pause['audio'], trigger = run_comp(
            win, Pause['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Pause['time']['audio'][0], duration=Pause['time']['audio'][1])

        waitOnFlip=False
        win, Pause['key_resp'], continueRoutine, endExpNow, trigger = run_comp(
            win, Pause['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Pause['time']['key_resp'][0], duration=Pause['time']['key_resp'][1],
            waitOnFlip=waitOnFlip)   
        # *Pause['cont']* updates
        win, Pause['cont'], trigger = run_comp(
            win, Pause['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Pause['time']['cont'][0], duration=Pause['time']['cont'][1],
            repeat_per_frame=True, repeat_content='Please have some rest and press space key to continue')

        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, PauseComponents)
        if break_flag:
            break
    # -------Ending Routine "Pause"-------
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Pause_cont.started', Pause['cont'].tStartRefresh)
    thisExp.addData('Pause_cont.stopped', Pause['cont'].tStopRefresh)

    thisExp = data_writer(thisExp, Pause, 'Pause', ['cont'])
    trigger_sending(61)
    # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


trigger_sending(1)  # Sending trigger 1 (Pre-Run End)
time.sleep(0.003)
# -----------------------------------------------------------------------------------
# ------------------------------ Start Run ------------------------------------------
# -----------------------------------------------------------------------------------


# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=n_run, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='run')
thisExp.addLoop(run)  # add the loop to the experiment
thisRun = run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in run:

    if break_run != None and run.thisN < break_run:
        continue
    break_run = None   # clear the breakpoint


    trigger_sending(4)   # Sending trigger 4 (Run Start)
    time.sleep(0.003)
    currentLoop = run

    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))

    # ---------------------------------------------------
    # --------------------- fade in ---------------------
    # ---------------------------------------------------
    if fade_in_flag:
        breakpoint_logger(comp='fade_in', value=1, run=run.thisN, block=None, trial=None)
        print('Log: fade in start: Run ' + str(run.thisN))
        if stim_freq == 0:
            trigger_sending(22)
            time.sleep(0.003)
            win.flip()
            time.sleep(60.000)
        else:
            if run.thisN == stim_run[0]:
                trigger_sending(20)
                fg = SG()
                fg.amp(init_intensity)
                fg.frequency(stim_freq)
                time.sleep(1.0)
                fg.on()
                time.sleep(1.0)

            if run.thisN == stim_run[0]:
                # ------Prepare to start Routine "fade_in"-------
                # keep track of which components have finished
                win, fade_in, fade_inComponents, t, frameN, continueRoutine = pre_run_comp(win, fade_in)
                trigger_mat = np.zeros((len(fade_inComponents) - 1, 2))
                comp_list = np.asarray([*fade_in['time'].keys()])
                # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=0)
                stim_continue = False
                trigger_sending(24)
                if run.thisN >= stim_run[0] + 1:
                    tmp_intensity = input_intensity
                    input_intensity = max_intensity - 0.05  # To be able to enter to loop of decreasing intensity
                while input_intensity < max_intensity and not stim_continue:
                    if run.thisN >= stim_run[0] + 1 and tmp_intensity != None:
                        input_intensity = tmp_intensity
                        tmp_intensity = None
                        print('initial ' + str(input_intensity))

                    fade_in_str = fade_str_func(intensity_goal[run.thisN])

                    if fade_in_out_show:
                        fade_in['text'].setText(fade_in_str + str(input_intensity*2) + 'mA')
                    else:
                        fade_in['text'].setText('')
                        # fade_in['text'].setText('The stimulation signal is fading in. Please remain seated and report any discomfort you may feel to the experimenter.')
                    routineTimer.reset()
                    routineTimer.add(2.000000)
                    intensity_change_flag = 'i'
                    # -------Run Routine "fade_in"-------
                    while continueRoutine and routineTimer.getTime() > 0:
                        # get current time
                        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                            fade_in["clock"], win, frameN)
                        # *fade_in["text"]* updates
                        win, fade_in['text'], trigger_mat[0] = run_comp(
                            win, fade_in['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                            start_time=fade_in['time']['text'][0], duration=fade_in['time']['text'][1])
                        
                        win, fade_in['auto_stim'], output_intensity, stim_continue, continueRoutine, endExpNow, intensity_change_flag, trigger_mat[1] = run_comp(
                            win, fade_in['auto_stim'], 'auto_stim', frameN, t, tThisFlip, tThisFlipGlobal, 
                            start_time=fade_in['time']['auto_stim'][0], duration=fade_in['time']['auto_stim'][1],
                            stim_current_intensity=input_intensity, stim_intensity_limit=[min_intensity, max_intensity],
                            stim_step_intensity=step_intensity, stim_obj=fg, intensity_change_flag=intensity_change_flag,
                            stim=True)

                        break_flag = False
                        win, continueRoutine, break_flag = continue_justification(
                            win, endExpNow, defaultKeyboard, continueRoutine, fade_inComponents)

                        if trigger_mat.sum(axis=0)[0]:
                            pass
                            # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=trigger_mat)
                        if break_flag:
                            break
                        input_intensity = output_intensity


                # -------Ending Routine "fade_in"-------
                for thisComponent in fade_inComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)

                thisExp = data_writer(thisExp, fade_in, 'fade_in', ['text'])
                trigger_sending(25)
                time.sleep(0.003)
            else:
                win.flip()
                time.sleep(30.000)

        print('Log: fade in end: Run ' + str(run.thisN))
        breakpoint_logger(comp='fade_in', value=0, run=run.thisN, block=None, trial=None)
        routineTimer.reset()
        trigger_sending(28)
        time.sleep(0.003)

    # ---------------------------------------------------
    # ---------------- Resting state --------------------
    # ---------------------------------------------------
    trigger_sending(6)
    time.sleep(0.003)
    RS_order = ['open', 'close']
    random.shuffle(RS_order)
    for RS_loop in range(2):

        if break_rs_block != None and RS_loop < break_rs_block:
            continue
        break_rs_block = None   # clear the breakpoint


        # ---------------------------------------------------
        # ------------------- RS_intro ----------------------
        # ---------------------------------------------------

        if RS_intro_flag:
            print('Log: RS intro start: Run ' + str(run.thisN) + RS_order[RS_loop] + ' Block ' + ': ' + str(RS_loop))
            breakpoint_logger(comp='RS_intro', value=1, run=run.thisN, block=RS_loop, trial=None)
            # ------Prepare to start Routine "RS_intro"-------
            RS_intro['audio'].setSound(audio_root+'resting_state/rs_intro_' + RS_order[RS_loop] + '.wav', secs=-1, hamming=True)
                
            # keep track of which components have finished
            win, RS_intro, RS_introComponents, t, frameN, continueRoutine = pre_run_comp(win, RS_intro)
            trigger_mat = np.zeros((len(RS_introComponents) - 1, 2))
            comp_list = np.asarray([*RS_intro['time'].keys()])
            trigger_sending(30)   # Sending trigger 30 (Resting State Intro Start)
            # -------Run Routine "RS_intro"-------
            while continueRoutine:
                # get current time
                frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                    RS_intro["clock"], win, frameN)

                # *RS_intro["title"]* updates
                win, RS_intro['title'], trigger_mat[0] = run_comp(
                    win, RS_intro['title'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_intro['time']['title'][0], duration=RS_intro['time']['title'][1])
                # *Cali_de_pre_intro["title"]* updates
                win, RS_intro['text'], trigger_mat[1] = run_comp(
                    win, RS_intro['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_intro['time']['text'][0], duration=RS_intro['time']['text'][1])
                # *Cali_de_pre_intro["audio"]* updates
                win, RS_intro['audio'], trigger_mat[2] = run_comp(
                    win, RS_intro['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_intro['time']['audio'][0], duration=RS_intro['time']['audio'][1])


                win, continueRoutine, break_flag = continue_justification(
                    win, endExpNow, defaultKeyboard, continueRoutine, RS_introComponents)
                
                if trigger_mat.sum(axis=0)[0]:
                    pass # trigger_encoding_sending('RS', input_run=run.thisRepN, input_block=0, intro_rec=0, input_event=trigger_mat)
                if break_flag:
                    break
            # trigger_encoding_sending('RS', input_run=run.thisRepN, input_block=0, intro_rec=0, input_event=2)
            # -------Ending Routine "RS_intro"-------
            for thisComponent in RS_introComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

            run = data_writer(run, RS_intro, 'RS_intro', ['title', 'text', 'audio'])
            trigger_sending(31)   # Sending trigger 30 (Resting State Intro End)
            # the Routine "RS_intro" was not non-slip safe, so reset the non-slip timer
            print('Log: RS intro finish: Run ' + str(run.thisN) + RS_order[RS_loop] + ' Block ' + ': ' + str(RS_loop))
            breakpoint_logger(comp='RS_intro', value=0, run=run.thisN, block=RS_loop, trial=None)
            routineTimer.reset()

        # ---------------------------------------------------
        # --------------------- RS_rec ----------------------
        # ---------------------------------------------------
        if RS_rec_flag:
            print('Log: RS rec start: Run ' + str(run.thisN) + RS_order[RS_loop] + ' Block ' + ': ' + str(RS_loop))
            breakpoint_logger(comp='RS_rec', value=1, run=run.thisN, block=RS_loop, trial=None)
            if RS_order[RS_loop] == 'open':
                trigger_sending(32)
                RS_rec_text_str = 'Please keep relaxed and open your eyes.\nNote: Blinking is allowed.'
                RS_rec['text'].setText(RS_rec_text_str)
            elif RS_order[RS_loop] == 'close':
                trigger_sending(34)
                RS_rec_text_str = 'Please keep relaxed and close your eyes.\n'
                RS_rec['text'].setText(RS_rec_text_str) 
            # ------Prepare to start Routine "RS_rec"-------
            # update component parameters for each repeat
            RS_rec['key_resp'].keys = []
            RS_rec['key_resp'].rt = []
            # keep track of which components have finished
            win, RS_rec, RS_recComponents, t, frameN, continueRoutine = pre_run_comp(win, RS_rec)
            trigger_mat = np.zeros((len(RS_recComponents) - 1, 2))
            comp_list = np.asarray([*RS_rec['time'].keys()])
            # trigger_encoding_sending('RS', input_run=run.thisRepN, input_block=0, intro_rec=1, input_event=0)
            # -------Run Routine "RS_rec"-------
            while continueRoutine:
                # get current time
                frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                    RS_rec["clock"], win, frameN)

                # *RS_rec["text"]* updates
                win, RS_rec['text'], trigger_mat[0] = run_comp(
                    win, RS_rec['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_rec['time']['text'][0], duration=RS_rec['time']['text'][1])
                # *Cali_de_pre_rec['key_resp']* updates
                waitOnFlip=False
                win, RS_rec['key_resp'], continueRoutine, endExpNow, trigger_mat[1] = run_comp(
                    win, RS_rec['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_rec['time']['key_resp'][0], duration=RS_rec['time']['key_resp'][1],
                    waitOnFlip=waitOnFlip)   
                # *Cali_de_pre_rec['cont']* updates
                win, RS_rec['cont'], trigger_mat[2] = run_comp(
                    win, RS_rec['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_rec['time']['cont'][0], duration=RS_rec['time']['cont'][1],
                    repeat_per_frame=True, repeat_content=continue_str)
                # *QA_rec["beep_end"]* updates
                win, RS_rec['beep_end'], trigger_mat[3] = run_comp(
                    win, RS_rec['beep_end'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=RS_rec['time']['beep_end'][0], duration=RS_rec['time']['beep_end'][1])

                win, continueRoutine, break_flag = continue_justification(
                    win, endExpNow, defaultKeyboard, continueRoutine, RS_recComponents)
                
                if trigger_mat.sum(axis=0)[0]:
                    pass # trigger_encoding_sending('RS', input_run=run.thisRepN, input_block=0, intro_rec=1, input_event=trigger_mat)
                if break_flag:
                    break
            # trigger_encoding_sending('RS', input_run=run.thisRepN, input_block=0, intro_rec=1, input_event=2)
            # -------Ending Routine "RS_rec"-------
            for thisComponent in RS_recComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            run = data_writer(run, RS_rec, 'RS_rec', ['text', 'cont'])
            if RS_order[RS_loop] == 'open':
                trigger_sending(33) 
            elif RS_order[RS_loop] == 'close':
                trigger_sending(35) 
            # the Routine "RS_rec" was not non-slip safe, so reset the non-slip timer
            print('Log: RS rec finish: Run ' + str(run.thisN) + RS_order[RS_loop] + ' Block ' + ': ' + str(RS_loop))
            breakpoint_logger(comp='RS_rec', value=0, run=run.thisN, block=RS_loop, trial=None)
            routineTimer.reset()

    # ---------------------------------------------------
    # --------------------- Pause -----------------------
    # ---------------------------------------------------
    if Pause_flag:
        trigger_sending(60)
        # ------Prepare to start Routine "Pause"-------
        # update component parameters for each repeat
        Pause['key_resp'].keys = []
        Pause['key_resp'].rt = []
        Pause['cont'].setText('Press [space] key to continue.')
        # keep track of which components have finished
        win, Pause, PauseComponents, t, frameN, continueRoutine = pre_run_comp(win, Pause)
        # -------Run Routine "Pause"-------
        while continueRoutine:
            # get current time
            frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                Pause["clock"], win, frameN)
            # update/draw components on each frame
            # *Pause['audio']* updates
            win, Pause['audio'], trigger = run_comp(
                win, Pause['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Pause['time']['audio'][0], duration=Pause['time']['audio'][1])

            waitOnFlip=False
            win, Pause['key_resp'], continueRoutine, endExpNow, trigger = run_comp(
                win, Pause['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Pause['time']['key_resp'][0], duration=Pause['time']['key_resp'][1],
                waitOnFlip=waitOnFlip)   
            # *Pause['cont']* updates
            win, Pause['cont'], trigger = run_comp(
                win, Pause['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Pause['time']['cont'][0], duration=Pause['time']['cont'][1],
                repeat_per_frame=True, repeat_content='Please have some rest and press space key to continue')

            win, continueRoutine, break_flag = continue_justification(
                win, endExpNow, defaultKeyboard, continueRoutine, PauseComponents)
            if break_flag:
                break
        # -------Ending Routine "Pause"-------
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pause_cont.started', Pause['cont'].tStartRefresh)
        thisExp.addData('Pause_cont.stopped', Pause['cont'].tStopRefresh)

        thisExp = data_writer(thisExp, Pause, 'Pause', ['cont'])
        trigger_sending(61)
        # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()




    time.sleep(0.003)
    trigger_sending(7)

    # ---------------------------------------------------
    # ------------------- QA_intro ----------------------
    # ---------------------------------------------------
    time.sleep(0.003)
    trigger_sending(40) 
    if QA_intro_flag:
        # ------Prepare to start Routine "QA_intro"-------
        # update component parameters for each repeat
        """
        QA_intro['audio'].setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/q_a/q_a.wav', secs=32, hamming=True)
        QA_intro['audio'].setVolume(1, log=False)
        """
        QA_intro['key_resp'].keys = []
        QA_intro['key_resp'].rt = []
        # keep track of which components have finished
        win, QA_intro, QA_introComponents, t, frameN, continueRoutine = pre_run_comp(win, QA_intro)
        trigger_mat = np.zeros((len(QA_introComponents) - 1, 2))
        comp_list = np.asarray([*QA_intro['time'].keys()])
        print('Log: QA intro start: Run ' + str(run.thisN))
        breakpoint_logger(comp='QA_intro', value=1, run=run.thisN, block=None, trial=None)
        # -------Run Routine "QA_intro"-------
        while continueRoutine:
            # get current time
            frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                QA_intro["clock"], win, frameN)
            # update/draw components on each frame

            # *RS_intro["title"]* updates
            win, QA_intro['title'], trigger_mat[0] = run_comp(
                win, QA_intro['title'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=QA_intro['time']['title'][0], duration=QA_intro['time']['title'][1])
            # *Cali_de_pre_intro["title"]* updates
            win, QA_intro['text'], trigger_mat[1] = run_comp(
                win, QA_intro['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=QA_intro['time']['text'][0], duration=QA_intro['time']['text'][1])
            # *Cali_de_pre_intro["audio"]* updates
            win, QA_intro['audio'], trigger_mat[2] = run_comp(
                win, QA_intro['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=QA_intro['time']['audio'][0], duration=QA_intro['time']['audio'][1])

            # *Cali_de_pre_intro['key_resp']* updates
            waitOnFlip=False
            win, QA_intro['key_resp'], continueRoutine, endExpNow, trigger_mat[3] = run_comp(
                win, QA_intro['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=QA_intro['time']['key_resp'][0], duration=QA_intro['time']['key_resp'][1],
                waitOnFlip=waitOnFlip)   
            # *Cali_de_pre_intro['cont']* updates
            win, QA_intro['cont'], trigger_mat[4] = run_comp(
                win, QA_intro['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=QA_intro['time']['cont'][0], duration=QA_intro['time']['cont'][1],
                repeat_per_frame=True, repeat_content=continue_str)

            win, continueRoutine, break_flag = continue_justification(
                win, endExpNow, defaultKeyboard, continueRoutine, QA_introComponents)
            
            if trigger_mat.sum(axis=0)[0]:
                pass
            if break_flag:
                break
        
        # -------Ending Routine "QA_intro"-------
        for thisComponent in QA_introComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        run = data_writer(run, QA_intro, 'QA_intro', ['title', 'text', 'audio', 'cont'])
        # the Routine "QA_intro" was not non-slip safe, so reset the non-slip timer
        print('Log: QA intro finish: Run ' + str(run.thisN))
        breakpoint_logger(comp='QA_intro', value=0, run=run.thisN, block=None, trial=None)
        routineTimer.reset()
    time.sleep(0.003)
    trigger_sending(41) 
    # -------------------------------------------------------------------------------
    # ------------------------------ Start Block ------------------------------------
    # -------------------------------------------------------------------------------
    # set up handler to look after randomisation of conditions etc
    if isinstance(n_block, list):
        n_block_parsed = n_block[run.thisRepN]
    else:
        n_block_parsed = n_block

    QA_block = data.TrialHandler(nReps=n_block_parsed, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='QA_block')
    thisExp.addLoop(QA_block)  # add the loop to the experiment
    thisQA_block = QA_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQA_block.rgb)
    if thisQA_block != None:
        for paramName in thisQA_block:
            exec('{} = thisQA_block[paramName]'.format(paramName))
    
    for thisQA_block in QA_block:

        if break_qa_block != None and QA_block.thisN < break_qa_block:
            continue
        break_qa_block = None   # clear the breakpoint


        time.sleep(0.003)
        trigger_sending(6)
        currentLoop = QA_block
        # abbreviate parameter names if possible (e.g. rgb = thisQA_block.rgb)
        if thisQA_block != None:
            for paramName in thisQA_block:
                exec('{} = thisQA_block[paramName]'.format(paramName))

        # ---------------------------------------------------------------------------
        # ------------------------------ Start Trial --------------------------------
        # ---------------------------------------------------------------------------
        # set up handler to look after randomisation of conditions etc

        QA_trial = data.TrialHandler(nReps=n_trial, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='QA_trial')
        thisExp.addLoop(QA_trial)  # add the loop to the experiment
        thisQA_trial = QA_trial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisQA_trial.rgb)
        if thisQA_trial != None:
            for paramName in thisQA_trial:
                exec('{} = thisQA_trial[paramName]'.format(paramName))
        
        for thisQA_trial in QA_trial:

            if break_qa_trial != None and QA_trial.thisN < break_qa_trial:
                continue
            if break_qa_trial != None:
                if RS_intro_flag == 0:
                    RS_intro_flag = 1
                if RS_rec_flag == 0:
                    RS_rec_flag = 1
                if QA_intro_flag == 0:
                    QA_intro_flag = 1

            break_qa_trial = None   # clear the breakpoint

            time.sleep(0.003)
            trigger_sending(42)
            currentLoop = QA_trial
            # abbreviate parameter names if possible (e.g. rgb = thisQA_trial.rgb)
            if thisQA_trial != None:
                for paramName in thisQA_trial:
                    exec('{} = thisQA_trial[paramName]'.format(paramName))
            
            # ---------------------------------------------------
            # -------------------- QA_rec -----------------------
            # ---------------------------------------------------

            if QA_rec_flag:
                print('Log: QA rec start: Run ' + str(run.thisN) + ' Block ' + str(QA_block.thisN) + 'Trial ' + str(QA_trial.thisN))
                breakpoint_logger(comp='QA_rec', value=1, run=run.thisN, block=QA_block.thisN, trial=QA_trial.thisN)
                # ------Prepare to start Routine "QA_rec"-------
                routineTimer.add(30.000000)
                # update component parameters for each repeat
                ques_start = QA_rec['time']['question'][0]
                if external_question_flag:
                    question_cnt += 1
                    QA_rec['question'].setSound(question_path[question_cnt], secs=14.4, hamming=True)
                    QA_rec['time']['question'][1] = sen_duration[question_cnt] - 0.016
                    QA_rec['time']['censor_word'] = [ques_start + censor_question_start[question_cnt], censor_question_duration[question_cnt]]
                    if flexible_qa_rec_start:
                        QA_trial_dur = 30.00
                        QA_rec['time']['beep_start'][0] = QA_q_start + sen_duration[question_cnt] + comp_gap
                        QA_rec['time']['recording'][0] = QA_rec['time']['beep_start'][0] + QA_a_beep_s_dur + comp_gap
                        QA_rec['time']['recording'][1] = QA_a_beep_e_start - QA_rec['time']['recording'][0] - comp_gap

                else:
                    QA_rec['question'].setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Database/old_data/article_0/sentence_0/sentence_0_syn_44100.wav', secs=-1, hamming=True)
                    QA_rec['time']['censor_word'] = [ques_start + 0.706, 0.694]
                    QA_rec['time']['question'][1] = 5.63 - 0.02




                # QA_rec['question'].setVolume(1, log=False)

                # keep track of which components have finished
                win, QA_rec, QA_recComponents, t, frameN, continueRoutine = pre_run_comp(win, QA_rec)
                trigger_mat = np.zeros((len(QA_recComponents) - 1, 2))
                comp_list = np.asarray([*QA_rec['time'].keys()])

                # -------Run Routine "QA_rec"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                        QA_rec["clock"], win, frameN)
                    # update/draw components on each frame

                    # *QA_rec["text"]* updates
                    win, QA_rec['text'], trigger_mat[0] = run_comp(
                        win, QA_rec['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['text'][0], duration=QA_rec['time']['text'][1])
                    # *QA_rec["beep_hint"]* updates
                    win, QA_rec['beep_hint'], trigger_mat[1] = run_comp(
                        win, QA_rec['beep_hint'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['beep_hint'][0], duration=QA_rec['time']['beep_hint'][1])
                    # *QA_rec["question"]* updates
                    win, QA_rec['question'], trigger_mat[2] = run_comp(
                        win, QA_rec['question'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['question'][0], duration=QA_rec['time']['question'][1])
                    # *QA_rec["beep_start"]* updates
                    win, QA_rec['beep_start'], trigger_mat[3] = run_comp(
                        win, QA_rec['beep_start'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['beep_start'][0], duration=QA_rec['time']['beep_start'][1])
                    # *QA_rec["recording"]* updates
                    win, QA_rec['recording'], trigger_mat[4] = run_comp(
                        win, QA_rec['recording'], 'recording', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['recording'][0], duration=QA_rec['time']['recording'][1])
                    # *QA_rec["beep_end"]* updates
                    win, QA_rec['beep_end'], trigger_mat[5] = run_comp(
                        win, QA_rec['beep_end'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['beep_end'][0], duration=QA_rec['time']['beep_end'][1])

                    win, QA_rec['break'], trigger_mat[6] = run_comp(
                        win, QA_rec['break'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['break'][0], duration=QA_rec['time']['break'][1])
                    win, QA_rec['censor_word'],temp_del =run_comp(
                        win, QA_rec['censor_word'], 'trigger', frameN, t, tThisFlip, tThisFlipGlobal, 
                        start_time=QA_rec['time']['censor_word'][0], duration=QA_rec['time']['censor_word'][1])

                    win, continueRoutine, break_flag = continue_justification(
                        win, endExpNow, defaultKeyboard, continueRoutine, QA_recComponents)
                    
                    if trigger_mat.sum(axis=0)[0]:
                        trigger_encoding_sending('QA', input_event=trigger_mat)
                    if break_flag:
                        break

                # -------Ending Routine "QA_rec"-------
                for thisComponent in QA_recComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                QA_trial = data_writer(QA_trial, QA_rec, 'QA_rec',
                    ['text', 'beep_hint', 'question', 'beep_start', 'beep_end', 'break'])
                q_a_rec_file = folder_path + 'rec_cali_de_pre.wav'
                q_a_rec_file = folder_path + 'rec_QA_run_' + str(run.thisN).zfill(2) + '_block_'+ str(QA_block.thisN).zfill(3) + '_trial_' + str(QA_trial.thisN).zfill(3)  + '.wav' 
                write(q_a_rec_file, fs, QA_rec['recording'].file)  # Save as WAV file 
                print('Recording is saved!' + q_a_rec_file)
                thisExp.addData('filename', q_a_rec_file)
                thisExp.nextEntry()
                print('Log: QA rec finish: Run ' + str(run.thisN) + ' Block ' + str(QA_block.thisN) + 'Trial ' + str(QA_trial.thisN))
                breakpoint_logger(comp='QA_rec', value=0, run=run.thisN, block=QA_block.thisN, trial=QA_trial.thisN)

            time.sleep(0.003)
            trigger_sending(43)
        
        time.sleep(0.003)
        trigger_sending(7)
        # completed 3 repeats of 'QA_trial'
        # ---------------------------------------------------
        # --------------------- Pause -----------------------
        # ---------------------------------------------------
        if Pause_flag:
            # ------Prepare to start Routine "Pause"-------
            # update component parameters for each repeat
            Pause['key_resp'].keys = []
            Pause['key_resp'].rt = []
            Pause['cont'].setText('Press [space] key to continue.')
            # keep track of which components have finished
            win, Pause, PauseComponents, t, frameN, continueRoutine = pre_run_comp(win, Pause)
            # -------Run Routine "Pause"-------
            while continueRoutine:
                # get current time
                frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                    Pause["clock"], win, frameN)
                # update/draw components on each frame
                # *Pause['audio']* updates
                win, Pause['audio'], trigger = run_comp(
                    win, Pause['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=Pause['time']['audio'][0], duration=Pause['time']['audio'][1])
                # *Cali_de_pre_intro['key_resp']* updates
                waitOnFlip=False
                win, Pause['key_resp'], continueRoutine, endExpNow, trigger = run_comp(
                    win, Pause['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=Pause['time']['key_resp'][0], duration=Pause['time']['key_resp'][1],
                    waitOnFlip=waitOnFlip)   
                # *Cali_de_pre_intro['cont']* updates
                win, Pause['cont'], trigger = run_comp(
                    win, Pause['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                    start_time=Pause['time']['cont'][0], duration=Pause['time']['cont'][1],
                    repeat_per_frame=True, repeat_content='Please have some rest and press space key to continue')

                win, continueRoutine, break_flag = continue_justification(
                    win, endExpNow, defaultKeyboard, continueRoutine, PauseComponents)
                if break_flag:
                    break
            # -------Ending Routine "Pause"-------
            for thisComponent in PauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            QA_block.addData('Pause_cont.started', Pause['cont'].tStartRefresh)
            QA_block.addData('Pause_cont.stopped', Pause['cont'].tStopRefresh)

            QA_block = data_writer(QA_block, Pause, 'Pause', ['cont'])
            # the Routine "Pause" was not non-slip safe, so reset the non-slip timer

            routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'QA_block'

    if fade_out_flag:
        print('Log: fade out start: Run ' + str(run.thisN))
        trigger_sending(29)
        time.sleep(0.003)

        time.sleep(60.000)
        if stim_freq == 0:
            trigger_sending(23)
            win.flip()

            time.sleep(60.000)
        else:
            if run.thisN == stim_run[-1]:
                # ------Prepare to start Routine "fade_in"-------
                
                # keep track of which components have finished
                win, fade_in, fade_inComponents, t, frameN, continueRoutine = pre_run_comp(win, fade_in)
                trigger_mat = np.zeros((len(fade_inComponents) - 1, 2))
                comp_list = np.asarray([*fade_in['time'].keys()])
                # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=0)
                stim_continue = False
                trigger_sending(26)
                if run.thisN >= stim_run[0] + 1:
                    tmp_intensity = input_intensity
                    input_intensity = max_intensity - 0.05  # To be able to enter to loop of decreasing intensity
                while input_intensity > min_intensity and not stim_continue:
                    if run.thisN >= stim_run[0] + 1 and tmp_intensity != None:
                        input_intensity = tmp_intensity
                        tmp_intensity = None
                        # print('initial ' + str(input_intensity))

                    fade_in_str = fade_str_func(intensity_goal[run.thisN + 1])
                    fade_in['text'].setText(fade_in_str + str(input_intensity*2) + 'mA')

                    if fade_in_out_show:
                        fade_in['text'].setText(fade_in_str + str(input_intensity*2) + 'mA')
                    else:
                        fade_in['text'].setText('The stimulation signal is fading out. Please remain seated and report any discomfort you may feel to the experimenter.')
                    

                    routineTimer.reset()
                    routineTimer.add(2.000000)
                    intensity_change_flag = 'd'
                    # -------Run Routine "fade_in"-------
                    while continueRoutine and routineTimer.getTime() > 0:
                        # get current time
                        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                            fade_in["clock"], win, frameN)
                        # *fade_in["text"]* updates
                        win, fade_in['text'], trigger_mat[0] = run_comp(
                            win, fade_in['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                            start_time=fade_in['time']['text'][0], duration=fade_in['time']['text'][1])
                        
                        win, fade_in['auto_stim'], output_intensity, stim_continue, continueRoutine, endExpNow, intensity_change_flag, trigger_mat[1] = run_comp(
                            win, fade_in['auto_stim'], 'auto_stim', frameN, t, tThisFlip, tThisFlipGlobal, 
                            start_time=fade_in['time']['auto_stim'][0], duration=fade_in['time']['auto_stim'][1],
                            stim_current_intensity=input_intensity, stim_intensity_limit=[min_intensity, max_intensity],
                            stim_step_intensity=step_intensity, stim_obj=fg, intensity_change_flag=intensity_change_flag,
                            stim=True)

                        break_flag = False
                        win, continueRoutine, break_flag = continue_justification(
                            win, endExpNow, defaultKeyboard, continueRoutine, fade_inComponents)

                        if trigger_mat.sum(axis=0)[0]:
                            pass
                            # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=trigger_mat)
                        if break_flag:
                            break

                        input_intensity = output_intensity
                    
                    # print('here input' + str(input_intensity))

                trigger_sending(27)
                time.sleep(0.003)
                # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=2)
                # -------Ending Routine "fade_in"-------
                for thisComponent in fade_inComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)

                thisExp = data_writer(thisExp, fade_in, 'fade_in', ['text'])
                
                if input_intensity > 0.05:
                    print('dangerous')
                    pdb.set_trace()
                else:
                    fg.off()


                trigger_sending(21)
                time.sleep(0.003)
            else:
                win.flip()
                time.sleep(30.000)
            routineTimer.reset()
        print('Log: fade out finish: Run ' + str(run.thisN))

    trigger_sending(5)   # Sending trigger 4 (Run End)
    time.sleep(0.003)
    thisExp.nextEntry()
    
# completed 3 repeats of 'run'


trigger_sending(2)  # Sending trigger 0 (Post-Run Start)
time.sleep(0.003)
# ---------------------------------------------------
# -------------- Cali_de_post_intro -----------------
# ---------------------------------------------------
if Cali_de_post_intro_flag:
    print('Log: cali_post_intro start')
    breakpoint_logger(comp='Cali_de_post_rec', value=1, run=None, block=None, trial=None)
    # ------Prepare to start Routine "Cali_de_post_intro"-------
    # update component parameters for each repeat
    Cali_de_post_intro['key_resp'].keys = []
    Cali_de_post_intro['key_resp'].rt = []
    # keep track of which components have finished
    win, Cali_de_post_intro, Cali_de_post_introComponents, t, frameN, continueRoutine = pre_run_comp(win, Cali_de_post_intro)
    trigger_mat = np.zeros((len(Cali_de_post_introComponents) - 1, 2))
    comp_list = np.asarray([*Cali_de_post_intro['time'].keys()])
    trigger_sending(10)  # Sending trigger 0 (Pre-Run Start)
    # -------Run Routine "Cali_de_post_intro"-------
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            Cali_de_post_intro["clock"], win, frameN)
        # update/draw components on each frame
        # *Cali_de_post_intro["title"]* updates
        win, Cali_de_post_intro['title'], trigger_mat[0] = run_comp(
            win, Cali_de_post_intro['title'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_post_intro['time']['title'][0], duration=Cali_de_post_intro['time']['title'][1])
        # *Cali_de_post_intro["title"]* updates
        win, Cali_de_post_intro['text'], trigger_mat[1] = run_comp(
            win, Cali_de_post_intro['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_post_intro['time']['text'][0], duration=Cali_de_post_intro['time']['text'][1])
        # *Cali_de_post_intro["audio"]* updates
        win, Cali_de_post_intro['audio'], trigger_mat[2] = run_comp(
            win, Cali_de_post_intro['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_post_intro['time']['audio'][0], duration=Cali_de_post_intro['time']['audio'][1])

        # *Cali_de_post_intro['key_resp']* updates
        waitOnFlip=False
        win, Cali_de_post_intro['key_resp'], continueRoutine, endExpNow, trigger_mat[3] = run_comp(
            win, Cali_de_post_intro['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_post_intro['time']['key_resp'][0], duration=Cali_de_post_intro['time']['key_resp'][1],
            waitOnFlip=waitOnFlip)   
        # *Cali_de_post_intro['cont']* updates
        win, Cali_de_post_intro['cont'], trigger_mat[4] = run_comp(
            win, Cali_de_post_intro['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Cali_de_post_intro['time']['cont'][0], duration=Cali_de_post_intro['time']['cont'][1],
            repeat_per_frame=True, repeat_content=continue_str)

        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, Cali_de_post_introComponents)
        
        if trigger_mat.sum(axis=0)[0]:
            pass # trigger_encoding_sending('Calibration', input_run=3, input_block=0, intro_rec=0, input_event=trigger_mat)
        if break_flag:
            break
    trigger_sending(11)  # Sending trigger 0 (Pre-Run Start)
    time.sleep(0.003)
    # -------Ending Routine "Cali_de_post_intro"-------
    for thisComponent in Cali_de_post_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp = data_writer(thisExp, Cali_de_post_intro, 'Cali_de_post_intro', ['title', 'text', 'audio', 'cont'])
    # the Routine "Cali_de_post_intro" was not non-slip safe, so reset the non-slip timer
    print('Log: cali_post_intro finish')
    breakpoint_logger(comp='Cali_de_post_rec', value=0, run=None, block=None, trial=None)
    routineTimer.reset()



# ---------------------------------------------------------------------------
# ------------------------ Start Calibration Trial --------------------------
# ---------------------------------------------------------------------------
# set up handler to look after randomisation of conditions etc

cali_post_trial = data.TrialHandler(nReps=n_cali_trial, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='post_trial')
thisExp.addLoop(cali_post_trial)  # add the loop to the experiment
thisCali_post_trial = cali_post_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCali_post_trial.rgb)
if thisCali_post_trial != None:
    for paramName in thisCali_post_trial:
        exec('{} = thisCali_post_trial[paramName]'.format(paramName))

for thisCali_post_trial in cali_post_trial:

    if break_cali_post_trial != None and cali_post_trial.thisN < break_cali_post_trial:
        continue

    currentLoop = cali_post_trial
    # abbreviate parameter names if possible (e.g. rgb = thisCali_post_trial.rgb)
    if thisCali_post_trial != None:
        for paramName in thisCali_post_trial:
            exec('{} = thisCali_post_trial[paramName]'.format(paramName))
    trigger_sending(12)
    time.sleep(0.003)
    # ---------------------------------------------------
    # --------------- Cali_de_post_rec -------------------
    # ---------------------------------------------------
    if Cali_de_post_rec_flag:
        print('Log: cali_post_rec start: Trial ' + str(cali_post_trial.thisN))
        breakpoint_logger(comp='Cali_de_post_rec', value=1, run=None, block=None, trial=cali_post_trial.thisN)
        # ------Prepare to start Routine "Cali_de_post_rec"-------
        # ------Prepare to start Routine "QA_rec"-------
        routineTimer.add(30.000000)
        # update component parameters for each repeat

        if external_question_flag:
            question_cnt += 1
            Cali_de_post_rec['question_text'].setText(sen_text[question_cnt])
        else:
            Cali_de_post_rec['question_text'].setText('Text ' + str(cali_post_trial.thisN))

        # update component parameters for each repeat 


        # keep track of which components have finished
        win, Cali_de_post_rec, Cali_de_post_recComponents, t, frameN, continueRoutine = pre_run_comp(win, Cali_de_post_rec)
        trigger_mat = np.zeros((len(Cali_de_post_recComponents) - 1, 2))
        comp_list = np.asarray([*Cali_de_post_rec['time'].keys()])
        # trigger_encoding_sending('Calibration', input_run=0, input_block=0, intro_rec=1, input_event=0)
        # -------Run Routine "Cali_de_post_rec"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
                Cali_de_post_rec["clock"], win, frameN)
            
            # *Cali_de_post_rec["text"]* updates
            win, Cali_de_post_rec['text'], trigger_mat[0] = run_comp(
                win, Cali_de_post_rec['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['text'][0], duration=Cali_de_post_rec['time']['text'][1])
            # *Cali_de_post_rec["beep_hint"]* updates
            win, Cali_de_post_rec['beep_hint'], trigger_mat[1] = run_comp(
                win, Cali_de_post_rec['beep_hint'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['beep_hint'][0], duration=Cali_de_post_rec['time']['beep_hint'][1])

            # *Cali_de_post_rec["question_text"]* updates
            win, Cali_de_post_rec['question_text'], trigger_mat[2] = run_comp(
                win, Cali_de_post_rec['question_text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['question_text'][0], duration=Cali_de_post_rec['time']['question_text'][1])

            # *Cali_de_post_rec["beep_start"]* updates
            win, Cali_de_post_rec['beep_start'], trigger_mat[3] = run_comp(
                win, Cali_de_post_rec['beep_start'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['beep_start'][0], duration=Cali_de_post_rec['time']['beep_start'][1])
            # *Cali_de_post_rec["recording"]* updates
            win, Cali_de_post_rec['recording'], trigger_mat[4] = run_comp(
                win, Cali_de_post_rec['recording'], 'recording', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['recording'][0], duration=Cali_de_post_rec['time']['recording'][1])
            # *Cali_de_post_rec["beep_end"]* updates
            win, Cali_de_post_rec['beep_end'], trigger_mat[5] = run_comp(
                win, Cali_de_post_rec['beep_end'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['beep_end'][0], duration=Cali_de_post_rec['time']['beep_end'][1])

            win, Cali_de_post_rec['break'], trigger_mat[6] = run_comp(
                win, Cali_de_post_rec['break'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
                start_time=Cali_de_post_rec['time']['break'][0], duration=Cali_de_post_rec['time']['break'][1])

            win, continueRoutine, break_flag = continue_justification(
                win, endExpNow, defaultKeyboard, continueRoutine, Cali_de_post_recComponents)

            if trigger_mat.sum(axis=0)[0]:
                trigger_encoding_sending('Calibration', input_event=trigger_mat)
            if break_flag:
                break
        # trigger_encoding_sending('Calibration', input_run=0, input_block=0, intro_rec=1, input_event=6)
        # -------Ending Routine "Cali_de_post_rec"-------
        for thisComponent in Cali_de_post_recComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        thisExp = data_writer(thisExp, Cali_de_post_rec, 'Cali_de_post_rec', ['text', 'beep_hint', 'question_text', 'beep_start', 'beep_end', 'break'])

        # cali_post_rec_file = folder_path + 'rec_cali_de_post_' + + ' .wav'
        cali_post_rec_file = folder_path + 'rec_cali_de_post_' + 'trial_' + str(cali_post_trial.thisN).zfill(3)  + '.wav' 
        write(cali_post_rec_file, fs, Cali_de_post_rec['recording'].file)  # Save as WAV file 
        print('Recording is saved!' + cali_post_rec_file)
        # Add the detected time into the PsychoPy data file:
        thisExp.addData('filename', cali_post_rec_file)
        
        thisExp.nextEntry()
        # the Routine "Cali_de_post_rec" was not non-slip safe, so reset the non-slip timer
        print('Log: cali_post_rec finish: Trial ' + str(cali_post_trial.thisN))
        breakpoint_logger(comp='Cali_de_post_rec', value=0, run=None, block=None, trial=cali_post_trial.thisN)
        routineTimer.reset()
    trigger_sending(13)
    time.sleep(0.003)


# ---------------------------------------------------
# --------------------- Pause -----------------------
# ---------------------------------------------------
if Pause_flag:
    trigger_sending(60)
    # ------Prepare to start Routine "Pause"-------
    # update component parameters for each repeat
    Pause['key_resp'].keys = []
    Pause['key_resp'].rt = []
    Pause['cont'].setText('Press [space] key to continue.')
    # keep track of which components have finished
    win, Pause, PauseComponents, t, frameN, continueRoutine = pre_run_comp(win, Pause)
    # -------Run Routine "Pause"-------
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            Pause["clock"], win, frameN)
        # update/draw components on each frame

        # *Cali_de_pre_intro['key_resp']* updates
        waitOnFlip=False
        win, Pause['key_resp'], continueRoutine, endExpNow, trigger = run_comp(
            win, Pause['key_resp'], 'key_resp', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Pause['time']['key_resp'][0], duration=Pause['time']['key_resp'][1],
            waitOnFlip=waitOnFlip)   
        # *Cali_de_pre_intro['cont']* updates
        win, Pause['cont'], trigger = run_comp(
            win, Pause['cont'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=Pause['time']['cont'][0], duration=Pause['time']['cont'][1],
            repeat_per_frame=True, repeat_content='Please have some rest and press space key to continue')

        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, PauseComponents)
        if break_flag:
            break
    # -------Ending Routine "Pause"-------
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Pause_cont.started', Pause['cont'].tStartRefresh)
    thisExp.addData('Pause_cont.stopped', Pause['cont'].tStopRefresh)

    thisExp = data_writer(thisExp, Pause, 'Pause', ['cont'])
    trigger_sending(61)
    # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

trigger_sending(3)  # Sending trigger 0 (Post-Run Finish)
time.sleep(0.003)


# ---------------------------------------------------
# ---------------------- End ------------------------
# ---------------------------------------------------
if end_flag:

    # ------Prepare to start Routine "the_end"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    win, the_end, the_endComponents, t, frameN, continueRoutine = pre_run_comp(win, the_end)
    # -------Run Routine "the_end"-------
    while continueRoutine:
        # get current time
        frameN, t, tThisFlip, tThisFlipGlobal, win = time_update(
            the_end["clock"], win, frameN)
        # update/draw components on each frame
        # *the_end['audio']* updates
        win, the_end['audio'], trigger = run_comp(
            win, the_end['audio'], 'audio', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=the_end['time']['audio'][0], duration=the_end['time']['audio'][1])

        # *the_end['cont']* updates
        win, the_end['text'], trigger = run_comp(
            win, the_end['text'], 'text', frameN, t, tThisFlip, tThisFlipGlobal, 
            start_time=the_end['time']['text'][0], duration=the_end['time']['text'][1],
            repeat_per_frame=True, repeat_content=the_end['text'].text)

        win, continueRoutine, break_flag = continue_justification(
            win, endExpNow, defaultKeyboard, continueRoutine, the_endComponents)
        if break_flag:
            break
    # -------Ending Routine "Pause"-------
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('the_end_text.started', the_end['text'].tStartRefresh)
    thisExp.addData('the_end_text.stopped', the_end['text'].tStopRefresh)

    thisExp = data_writer(thisExp, the_end, 'the_end', ['text'])

    # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
trigger_sending(255)









# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
