#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on Sun 29 Dec 2019 05:03:27 PM CET
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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
from pdb import set_trace
import ctypes
xlib = ctypes.cdll.LoadLibrary("libX11.so")
xlib.XInitThreads()
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=32)

# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler
import sounddevice as sd
from scipy.io.wavfile import write


def exp_init():
    # -----------------------------------------------------------------------------------
    # -------------------- Experiment & Device initialization ---------------------------
    # -----------------------------------------------------------------------------------
    # Store info about the experiment session
    expName = 'nibs_stage_1'  # from the Builder filename that created this script
    Info = {'participant': '001', 'session': '001', 'First language':'', 'German level':''}
    dlg = gui.DlgFromDict(dictionary=Info, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    Info['date'] = data.getDateStr()  # add a simple timestamp
    Info['expName'] = expName
    Info['psychopyVersion'] = '3.2.3'

    # Setup the Window
    win = visual.Window(
        size=[1920, 1080], fullscr=False, screen=0, 
        winType='pyglet', allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True)
    # store frame rate of monitor if we can measure it
    Info['frameRate'] = win.getActualFrameRate()
    if Info['frameRate'] != None:
        frameDur = 1.0 / round(Info['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard()
    
    return Info, win, frameDur, defaultKeyboard 


def create_folder(folder_path):
    # copy from "from jxu.basiccmd.cmd import create_folder" 
    if os.path.exists(folder_path):
        return print("Traget folder is already created! Path: \n" + folder_path)
    else:
        try:
            os.mkdir(folder_path)
        except:
            path = os.path.normpath(folder_path)
            path_seg = path.split(os.sep)
            if len(path_seg) == 0:
                raise ValueError("Empty path of target folder!")

            for subfolder_path in path_seg:
                if not os.path.exists(subfolder_path):
                    os.mkdir(subfolder_path)
                os.chdir(subfolder_path)
            os.chdir(os.path.dirname(os.path.abspath(os.getcwd())))

        return print("Target folder is successfully created! Path: \n" + folder_path)

def path_init():
    # -----------------------------------------------------------------------------------
    # ----------------------- Folder & File initialization ------------------------------
    # -----------------------------------------------------------------------------------
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)

    folder_path = './data/Subject_%s/Session_%s/Exp_data' %(
        expInfo['participant'], expInfo['session'])
    filename = _thisDir + os.sep + 'data/Subject_%s/Session_%s/%s_%s' %(
        expInfo['participant'], expInfo['session'], expInfo['expName'], expInfo['date'])
    create_folder(folder_path)

    return folder_path, filename


def component_init(routine, comp, comp_index):
    if comp['property'] == 'textstim':
        return visual.TextStim(name=routine + '_' + comp['comp_name'],
                               depth=-np.float(comp_index),
                               **comp['parameters'])
    elif comp['property'] == 'keyboard':
        return keyboard.Keyboard(**comp['parameters'])
    elif comp['property'] == 'audio':
        return sound.Sound(name=routine + '_' + comp['comp_name'],
                           **comp['parameters'])
    elif comp['property'] == 'textstim':
        pass
    elif comp['property'] == 'textstim':
        pass
    elif comp['property'] == 'textstim':
        pass
    elif comp['property'] == 'textstim':
        pass
    else:
        pass


def routine_init(routine_name, comp_list):
    routine = {}
    routine["clock"] = core.Clock()
    for comp_ind, comp in enumerate(comp_list):
        routine[comp['comp_name']] = component_init(routine_name, comp, comp_ind)
    return routine


def textstim_generator(win, name, content='', pos=[0.5, 0.0], font_size=0.06, font_type='Arial', bold=False):
    dict_textstim = {
        'property':'textstim',
        'comp_name': name,
        'parameters':{'win': win,
                      'text':content,
                      'pos': pos,
                      'height': font_size,
                      'font': font_type,
                      'bold': bold}
        }
    return dict_textstim


def key_resp_generator(name):
    dict_key_resp = {
        'property':'keyboard',
        'comp_name': name,
        'parameters':{}
        }
    return dict_key_resp

def audio_generator(name, loc, secs=-1, vol=1.0, sr=44100, stereo=True, hamming=True):
    dict_audio = {
        'property':'audio',
        'comp_name': name,
        'parameters':{'volume':vol,
                      'sampleRate': sr,
                      'stereo': stereo,
                      'hamming': hamming,
                      'secs': secs}
        }
    return dict_audio
# -----------------------------------------------------------------------------------
# ------------------------- Setting: Parameter --------------------------------------
# -----------------------------------------------------------------------------------

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
continue_str = 'Press [space] key to continue.'
font_type = 'Airal'
font_size = 0.06  # font size

title_pos = [0.5, 0.3]
text_pos = [0.5, 0]
annot_pos = [0.5, -0.3]
audio_root = '../../../../Data/NIBS/Stage_one/Audio/Soundeffect/'


# -----------------------------------------------------------------------------------
# ------------------------ Setting: Initialization ----------------------------------
# -----------------------------------------------------------------------------------
expInfo, win, frameDur, defaultKeyboard  = exp_init()
folder_path, filename = path_init()

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file





win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# -----------------------------------------------------------------------------------
# ------------------------------ Start Code -----------------------------------------
# -----------------------------------------------------------------------------------
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expInfo['expName'], version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='nibs_minimal_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

instruction_text_str = 'Welcome to participate our experiment: causal ' + \
    'prediction model for non-invasive ' + \
    'brain stimulation\n\nTask introductrion: \n\n'
instruction_comp_list = [
    textstim_generator(win=win, name='text', content=instruction_text_str, pos=text_pos),
    key_resp_generator(name='key_resp'),
    textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
    ]
instruction = routine_init('instruction', instruction_comp_list)

"""
Cali_de_pre_intro = routine_init('Cali_de_pre_intro', Cali_de_pre_intro_comp_list)
Cali_de_post_intro = routine_init('Cali_de_post_intro', Cali_de_post_intro_comp_list)
Cali_de_pre_intro = routine_init('Cali_de_pre_intro', Cali_de_pre_intro_comp_list)
Cali_de_pre_intro = routine_init('Cali_de_pre_intro', Cali_de_pre_intro_comp_list)
"""

# Initialize components for Routine "Cali_de_pre_intro"

Cali_de_pre_intro_text_str = '1. Several sentences written in German on the screen,' + \
    ' and please read out them loudly after hearing an increasing tonal beeping sound.\n ' + \
    '2. A decreasing tonal beeping sound indicates the recording is finished.'
Cali_de_pre_intro_comp_list = [
    textstim_generator(win=win, name='title', content='READ OUT BLOCK (GERMAN)', pos=title_pos),
    textstim_generator(win=win, name='text', content=Cali_de_pre_intro_text_str, pos=text_pos),
    audio_generator(name='audio', loc=audio_root+'calibration/cali_de.wav', secs=-1),
    key_resp_generator(name='key_resp'),
    textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
    ]
Cali_de_pre_intro = routine_init('Cali_de_pre_intro', Cali_de_pre_intro_comp_list)


# Initialize components for Routine "Cali_de_pre_rec"


Cali_de_pre_rec_text_str = 'Hallo, Ich bin Chen aus Wien.'
Cali_de_pre_rec_comp_list = [
    textstim_generator(win=win, name='text', content=Cali_de_pre_rec_text_str, pos=text_pos),
    audio_generator(name='beep_hint', loc=audio_root+'calibration/C5_A_tone_flat_half_s.wav', secs=0.6),
    audio_generator(name='beep_start', loc=audio_root+'calibration/C3A_C4A_tone_decrease_1s.wav', secs=1),
    audio_generator(name='beep_end', loc=audio_root+'calibration/C4A_C3A_tone_decrease_1s.wav', secs=1),
    key_resp_generator(name='key_resp'),
    textstim_generator(win=win, name='cont', content=continue_str, pos=annot_pos)
    ]
Cali_de_pre_rec = routine_init('Cali_de_pre_intro', Cali_de_pre_rec_comp_list)



Cali_de_pre_recClock = core.Clock()
Cali_de_pre_rec_text = visual.TextStim(win=win, name='Cali_de_pre_rec_text',
    text='Hallo, Ich bin Chen aus Wien.',
    font='Arial',
    pos=(0.5, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cali_de_pre_rec_beep_hint = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, stereo=True, hamming=True,
    name='Cali_de_pre_rec_beep_hint')
Cali_de_pre_rec_beep_hint.setVolume(1)
Cali_de_pre_rec_beep_start = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='Cali_de_pre_rec_beep_start')
Cali_de_pre_rec_beep_start.setVolume(1)
Cali_de_pre_rec_beep_end = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='Cali_de_pre_rec_beep_end')
Cali_de_pre_rec_beep_end.setVolume(1)
Cali_de_pre_rec_key_resp = keyboard.Keyboard()
Cali_de_pre_rec_cont = visual.TextStim(win=win, name='Cali_de_pre_rec_cont',
    text='Press [space] key to continue.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "RS_intro"
RS_introClock = core.Clock()
RS_intro_title = visual.TextStim(win=win, name='RS_intro_title',
    text='REST STATE BLOCK\n',
    font='Arial',
    pos=[0.5, 0.5], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RS_intro_text = visual.TextStim(win=win, name='RS_intro_text',
    text='1. Please remain seated and keep relaxed while opening your eyes.\n2. A decreasing tonal beeping sound will be played to indicate this block is finished',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
RS_intro_audio_close = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/resting_state/rs_close.wav', secs=-1, stereo=True, hamming=True,
    name='RS_intro_audio_close')
RS_intro_audio_close.setVolume(1)
RS_intro_key_resp = keyboard.Keyboard()
RS_intro_cont = visual.TextStim(win=win, name='RS_intro_cont',
    text='Press [space] key to continue.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "RS_rec"
RS_recClock = core.Clock()
RS_rec_text = visual.TextStim(win=win, name='RS_rec_text',
    text='Please keep relaxed and open your eyes.\nNote: Blinking is allowed.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RS_rec_key_resp = keyboard.Keyboard()
RS_rec_cont = visual.TextStim(win=win, name='RS_rec_cont',
    text='Press [space] key to continue.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "QA_intro"
QA_introClock = core.Clock()
QA_intro_title = visual.TextStim(win=win, name='QA_intro_title',
    text='Q&A BLOCK',
    font='Arial',
    pos=[0.5, 0.5], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
QA_intro_text = visual.TextStim(win=win, name='QA_intro_text',
    text='1. You will hear one German sentence with a censored missing word in every trial and you are expected to fill this sentence.\n2. These sentences will be played after a flat tonal beeping.\n3. You should speak out your answer after hearing an increasing tonal beeping.\n4. A decreasing tonal beeping sound indicates this trial is finished.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
QA_intro_audio = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/q_a/q_a.wav', secs=-1, stereo=True, hamming=True,
    name='QA_intro_audio')
QA_intro_audio.setVolume(1)
QA_intro_key_resp = keyboard.Keyboard()
QA_intro_cont = visual.TextStim(win=win, name='QA_intro_cont',
    text='default text',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "QA_rec"
QA_recClock = core.Clock()
QA_rec_text = visual.TextStim(win=win, name='QA_rec_text',
    text='Listening to the question and speaking out your answer!',
    font='Arial',
    pos=(0.5, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
QA_rec_beep_hint = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, stereo=True, hamming=True,
    name='QA_rec_beep_hint')
QA_rec_beep_hint.setVolume(1)
QA_rec_question = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Database/article_0/sentence_0/sentence_0_syn.wav', secs=-1, stereo=True, hamming=True,
    name='QA_rec_question')
QA_rec_question.setVolume(1)
QA_rec_beep_start = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='QA_rec_beep_start')
QA_rec_beep_start.setVolume(1)
QA_rec_beep_end = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='QA_rec_beep_end')
QA_rec_beep_end.setVolume(1)
QA_rec_break = visual.TextStim(win=win, name='QA_rec_break',
    text='Short break',
    font='Arial',
    pos=[0.5,0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
Pause_key_resp = keyboard.Keyboard()
Pause_text = visual.TextStim(win=win, name='Pause_text',
    text='default text',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Cali_de_post_intro"
Cali_de_post_introClock = core.Clock()
Cali_de_post_intro_title = visual.TextStim(win=win, name='Cali_de_post_intro_title',
    text='READ OUT BLOCK (GERMAN)',
    font='Arial',
    pos=[0.5, 0.5], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cali_de_post_intro_text = visual.TextStim(win=win, name='Cali_de_post_intro_text',
    text='1. Several sentences written in German on the screen, and please read out them loudly after hearing an increasing tonal beeping sound.\n2. A decreasing tonal beeping sound indicates the recording is finished.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Cali_de_post_intro_audio = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/cali_de.wav', secs=-1, stereo=True, hamming=True,
    name='Cali_de_post_intro_audio')
Cali_de_post_intro_audio.setVolume(1)
Cali_de_post_intro_key_resp = keyboard.Keyboard()
Cali_de_post_intro_cont = visual.TextStim(win=win, name='Cali_de_post_intro_cont',
    text='default text',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Cali_de_post_rec"
Cali_de_post_recClock = core.Clock()
Cali_de_post_rec_text = visual.TextStim(win=win, name='Cali_de_post_rec_text',
    text='Hallo, Ich bin Chen aus Wien.',
    font='Arial',
    pos=(0.5, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cali_de_post_rec_beep_hint = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, stereo=True, hamming=True,
    name='Cali_de_post_rec_beep_hint')
Cali_de_post_rec_beep_hint.setVolume(1)
Cali_de_post_rec_beep_start = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='Cali_de_post_rec_beep_start')
Cali_de_post_rec_beep_start.setVolume(1)
Cali_de_post_rec_beep_end = sound.Sound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, stereo=True, hamming=True,
    name='Cali_de_post_rec_beep_end')
Cali_de_post_rec_beep_end.setVolume(1)
Cali_de_post_rec_key_resp = keyboard.Keyboard()
Cali_de_post_rec_cont = visual.TextStim(win=win, name='Cali_de_post_rec_cont',
    text='Press [space] key to continue.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "the_end"
the_endClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='The end.\n\nData + recordings are in folder data/',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
# update component parameters for each repeat
instruction['key_resp'].keys = []
instruction['key_resp'].rt = []
# keep track of which components have finished
instructionComponents = [instruction['text'], instruction['key_resp'], instruction['cont']]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction["clock"].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instruction["clock"].getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction["clock"])
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction["text"]* updates
    if instruction['text'].status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instruction['text'].frameNStart = frameN  # exact frame index
        instruction['text'].tStart = t  # local t and not account for scr refresh
        instruction['text'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction['text'], 'tStartRefresh')  # time at next scr refresh
        instruction['text'].setAutoDraw(True)
    
    # *instruction['key_resp']* updates
    waitOnFlip = False
    if instruction['key_resp'].status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        instruction['key_resp'].frameNStart = frameN  # exact frame index
        instruction['key_resp'].tStart = t  # local t and not account for scr refresh
        instruction['key_resp'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction['key_resp'], 'tStartRefresh')  # time at next scr refresh
        instruction['key_resp'].status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruction['key_resp'].clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction['key_resp'].status == STARTED and not waitOnFlip:
        theseKeys = instruction['key_resp'].getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruction['cont']* updates
    if instruction['cont'].status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        instruction['cont'].frameNStart = frameN  # exact frame index
        instruction['cont'].tStart = t  # local t and not account for scr refresh
        instruction['cont'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction['cont'], 'tStartRefresh')  # time at next scr refresh
        instruction['cont'].setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("instruction['text'].started", instruction['text'].tStartRefresh)
thisExp.addData("instruction['text'].stopped", instruction['text'].tStopRefresh)
thisExp.addData("instruction['cont'].started", instruction['cont'].tStartRefresh)
thisExp.addData("instruction['cont'].stopped", instruction['cont'].tStopRefresh)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cali_de_pre_intro"-------
# update component parameters for each repeat
Cali_de_pre_intro['audio'].setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/cali_de.wav', secs=23, hamming=True)
Cali_de_pre_intro['audio'].setVolume(1, log=False)
Cali_de_pre_intro['key_resp'].keys = []
Cali_de_pre_intro['key_resp'].rt = []
# keep track of which components have finished
Cali_de_pre_introComponents = [Cali_de_pre_intro['title'], Cali_de_pre_intro['text'], Cali_de_pre_intro['audio'], Cali_de_pre_intro['key_resp'], Cali_de_pre_intro['cont']]
for thisComponent in Cali_de_pre_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Cali_de_pre_intro['clock'].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Cali_de_pre_intro"-------
while continueRoutine:
    # get current time
    t = Cali_de_pre_intro['clock'].getTime()
    tThisFlip = win.getFutureFlipTime(clock=Cali_de_pre_intro['clock'])
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cali_de_pre_intro['title']* updates
    if Cali_de_pre_intro['title'].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro['title'].frameNStart = frameN  # exact frame index
        Cali_de_pre_intro['title'].tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro['title'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro['title'], 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro['title'].setAutoDraw(True)
    if Cali_de_pre_intro['title'].status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro['title'].tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro['title'].tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro['title'].frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro['title'], 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro['title'].setAutoDraw(False)
    
    # *Cali_de_pre_intro['text']* updates
    if Cali_de_pre_intro['text'].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro['text'].frameNStart = frameN  # exact frame index
        Cali_de_pre_intro['text'].tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro['text'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro['text'], 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro['text'].setAutoDraw(True)
    if Cali_de_pre_intro['text'].status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro['text'].tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro['text'].tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro['text'].frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro['text'], 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro['text'].setAutoDraw(False)
    # start/stop Cali_de_pre_intro['audio']
    if Cali_de_pre_intro['audio'].status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro['audio'].frameNStart = frameN  # exact frame index
        Cali_de_pre_intro['audio'].tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro['audio'].tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_pre_intro['audio'].play(when=win)  # sync with win flip
    if Cali_de_pre_intro['audio'].status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro['audio'].tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro['audio'].tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro['audio'].frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro['audio'], 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro['audio'].stop()
    
    # *Cali_de_pre_intro['key_resp']* updates
    waitOnFlip = False
    if Cali_de_pre_intro['key_resp'].status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro['key_resp'].frameNStart = frameN  # exact frame index
        Cali_de_pre_intro['key_resp'].tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro['key_resp'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro['key_resp'], 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro['key_resp'].status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Cali_de_pre_intro['key_resp'].clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Cali_de_pre_intro['key_resp'].status == STARTED and not waitOnFlip:
        theseKeys = Cali_de_pre_intro['key_resp'].getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Cali_de_pre_intro['cont']* updates
    if Cali_de_pre_intro['cont'].status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro['cont'].frameNStart = frameN  # exact frame index
        Cali_de_pre_intro['cont'].tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro['cont'].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro['cont'], 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro['cont'].setAutoDraw(True)
    if Cali_de_pre_intro['cont'].status == STARTED:  # only update if drawing
        Cali_de_pre_intro['cont'].setText('Press [space] key to continue.', log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cali_de_pre_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cali_de_pre_intro"-------
for thisComponent in Cali_de_pre_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("Cali_de_pre_intro['title'].started", Cali_de_pre_intro['title'].tStartRefresh)
thisExp.addData("Cali_de_pre_intro['title'].stopped", Cali_de_pre_intro['title'].tStopRefresh)
thisExp.addData("Cali_de_pre_intro['text'].started", Cali_de_pre_intro['text'].tStartRefresh)
thisExp.addData("Cali_de_pre_intro['text'].stopped", Cali_de_pre_intro['text'].tStopRefresh)
Cali_de_pre_intro['audio'].stop()  # ensure sound has stopped at end of routine
thisExp.addData("Cali_de_pre_intro['audio'].started", Cali_de_pre_intro['audio'].tStartRefresh)
thisExp.addData("Cali_de_pre_intro['audio'].stopped", Cali_de_pre_intro['audio'].tStopRefresh)
thisExp.addData("Cali_de_pre_intro['cont'].started", Cali_de_pre_intro['cont'].tStartRefresh)
thisExp.addData("Cali_de_pre_intro['cont'].stopped", Cali_de_pre_intro['cont'].tStopRefresh)
# the Routine "Cali_de_pre_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cali_de_pre_rec"-------
# update component parameters for each repeat
Cali_de_pre_rec_beep_hint.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, hamming=True)
Cali_de_pre_rec_beep_hint.setVolume(1, log=False)
Cali_de_pre_rec_beep_start.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, hamming=True)
Cali_de_pre_rec_beep_start.setVolume(1, log=False)


# Create a voice-key to be used:
file_name ='data/rec_cali_de_pre.wav'
fs = 44100  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#  sd.wait()  # Wait until recording is finished

Cali_de_pre_rec_beep_end.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, hamming=True)
Cali_de_pre_rec_beep_end.setVolume(1, log=False)
Cali_de_pre_rec_key_resp.keys = []
Cali_de_pre_rec_key_resp.rt = []
# keep track of which components have finished
Cali_de_pre_recComponents = [Cali_de_pre_rec_text, Cali_de_pre_rec_beep_hint, Cali_de_pre_rec_beep_start, Cali_de_pre_rec_beep_end, Cali_de_pre_rec_key_resp, Cali_de_pre_rec_cont]
for thisComponent in Cali_de_pre_recComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Cali_de_pre_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Cali_de_pre_rec"-------
while continueRoutine:
    # get current time
    t = Cali_de_pre_recClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Cali_de_pre_recClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cali_de_pre_rec_text* updates
    if Cali_de_pre_rec_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_text.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_text.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_rec_text, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_rec_text.setAutoDraw(True)
    if Cali_de_pre_rec_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_rec_text.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_rec_text.tStop = t  # not accounting for scr refresh
            Cali_de_pre_rec_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_rec_text, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_rec_text.setAutoDraw(False)
    # start/stop Cali_de_pre_rec_beep_hint
    if Cali_de_pre_rec_beep_hint.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_beep_hint.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_beep_hint.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_beep_hint.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_pre_rec_beep_hint.play(when=win)  # sync with win flip
    if Cali_de_pre_rec_beep_hint.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_rec_beep_hint.tStartRefresh + 0.6-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_rec_beep_hint.tStop = t  # not accounting for scr refresh
            Cali_de_pre_rec_beep_hint.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_rec_beep_hint, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_rec_beep_hint.stop()
    # start/stop Cali_de_pre_rec_beep_start
    if Cali_de_pre_rec_beep_start.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_beep_start.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_beep_start.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_beep_start.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_pre_rec_beep_start.play(when=win)  # sync with win flip
    if Cali_de_pre_rec_beep_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_rec_beep_start.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_rec_beep_start.tStop = t  # not accounting for scr refresh
            Cali_de_pre_rec_beep_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_rec_beep_start, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_rec_beep_start.stop()
    # Nothing needed every frame for this demo
    # start/stop Cali_de_pre_rec_beep_end
    if Cali_de_pre_rec_beep_end.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_beep_end.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_beep_end.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_beep_end.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_pre_rec_beep_end.play(when=win)  # sync with win flip
    if Cali_de_pre_rec_beep_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_rec_beep_end.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_rec_beep_end.tStop = t  # not accounting for scr refresh
            Cali_de_pre_rec_beep_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_rec_beep_end, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_rec_beep_end.stop()
    
    # *Cali_de_pre_rec_key_resp* updates
    waitOnFlip = False
    if Cali_de_pre_rec_key_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_key_resp.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_key_resp.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_rec_key_resp, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_rec_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Cali_de_pre_rec_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Cali_de_pre_rec_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Cali_de_pre_rec_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Cali_de_pre_rec_cont* updates
    if Cali_de_pre_rec_cont.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_rec_cont.frameNStart = frameN  # exact frame index
        Cali_de_pre_rec_cont.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_rec_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_rec_cont, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_rec_cont.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cali_de_pre_recComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cali_de_pre_rec"-------
for thisComponent in Cali_de_pre_recComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Cali_de_pre_rec_text.started', Cali_de_pre_rec_text.tStartRefresh)
thisExp.addData('Cali_de_pre_rec_text.stopped', Cali_de_pre_rec_text.tStopRefresh)
Cali_de_pre_rec_beep_hint.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_pre_rec_beep_hint.started', Cali_de_pre_rec_beep_hint.tStartRefresh)
thisExp.addData('Cali_de_pre_rec_beep_hint.stopped', Cali_de_pre_rec_beep_hint.tStopRefresh)
Cali_de_pre_rec_beep_start.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_pre_rec_beep_start.started', Cali_de_pre_rec_beep_start.tStartRefresh)
thisExp.addData('Cali_de_pre_rec_beep_start.stopped', Cali_de_pre_rec_beep_start.tStopRefresh)

write(file_name, fs, myrecording)  # Save as WAV file 
# Add the detected time into the PsychoPy data file:
# thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
# thisExp.addData('bad_baseline', vpvk.bad_baseline)
thisExp.addData('filename', file_name)
thisExp.nextEntry()
Cali_de_pre_rec_beep_end.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_pre_rec_beep_end.started', Cali_de_pre_rec_beep_end.tStartRefresh)
thisExp.addData('Cali_de_pre_rec_beep_end.stopped', Cali_de_pre_rec_beep_end.tStopRefresh)
thisExp.addData('Cali_de_pre_rec_cont.started', Cali_de_pre_rec_cont.tStartRefresh)
thisExp.addData('Cali_de_pre_rec_cont.stopped', Cali_de_pre_rec_cont.tStopRefresh)
# the Routine "Cali_de_pre_rec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=3, method='random', 
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
    currentLoop = run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RS_intro"-------
    # update component parameters for each repeat
    RS_intro_audio_close.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/resting_state/rs_close.wav', secs=14, hamming=True)
    RS_intro_audio_close.setVolume(1, log=False)
    RS_intro_key_resp.keys = []
    RS_intro_key_resp.rt = []
    # keep track of which components have finished
    RS_introComponents = [RS_intro_title, RS_intro_text, RS_intro_audio_close, RS_intro_key_resp, RS_intro_cont]
    for thisComponent in RS_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RS_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "RS_intro"-------
    while continueRoutine:
        # get current time
        t = RS_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RS_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RS_intro_title* updates
        if RS_intro_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RS_intro_title.frameNStart = frameN  # exact frame index
            RS_intro_title.tStart = t  # local t and not account for scr refresh
            RS_intro_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_intro_title, 'tStartRefresh')  # time at next scr refresh
            RS_intro_title.setAutoDraw(True)
        if RS_intro_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RS_intro_title.tStartRefresh + 14-frameTolerance:
                # keep track of stop time/frame for later
                RS_intro_title.tStop = t  # not accounting for scr refresh
                RS_intro_title.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RS_intro_title, 'tStopRefresh')  # time at next scr refresh
                RS_intro_title.setAutoDraw(False)
        
        # *RS_intro_text* updates
        if RS_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RS_intro_text.frameNStart = frameN  # exact frame index
            RS_intro_text.tStart = t  # local t and not account for scr refresh
            RS_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_intro_text, 'tStartRefresh')  # time at next scr refresh
            RS_intro_text.setAutoDraw(True)
        if RS_intro_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RS_intro_text.tStartRefresh + 14-frameTolerance:
                # keep track of stop time/frame for later
                RS_intro_text.tStop = t  # not accounting for scr refresh
                RS_intro_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RS_intro_text, 'tStopRefresh')  # time at next scr refresh
                RS_intro_text.setAutoDraw(False)
        # start/stop RS_intro_audio_close
        if RS_intro_audio_close.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RS_intro_audio_close.frameNStart = frameN  # exact frame index
            RS_intro_audio_close.tStart = t  # local t and not account for scr refresh
            RS_intro_audio_close.tStartRefresh = tThisFlipGlobal  # on global time
            RS_intro_audio_close.play(when=win)  # sync with win flip
        if RS_intro_audio_close.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RS_intro_audio_close.tStartRefresh + 14-frameTolerance:
                # keep track of stop time/frame for later
                RS_intro_audio_close.tStop = t  # not accounting for scr refresh
                RS_intro_audio_close.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RS_intro_audio_close, 'tStopRefresh')  # time at next scr refresh
                RS_intro_audio_close.stop()
        
        # *RS_intro_key_resp* updates
        waitOnFlip = False
        if RS_intro_key_resp.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            RS_intro_key_resp.frameNStart = frameN  # exact frame index
            RS_intro_key_resp.tStart = t  # local t and not account for scr refresh
            RS_intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_intro_key_resp, 'tStartRefresh')  # time at next scr refresh
            RS_intro_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(RS_intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RS_intro_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = RS_intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *RS_intro_cont* updates
        if RS_intro_cont.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            RS_intro_cont.frameNStart = frameN  # exact frame index
            RS_intro_cont.tStart = t  # local t and not account for scr refresh
            RS_intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_intro_cont, 'tStartRefresh')  # time at next scr refresh
            RS_intro_cont.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RS_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RS_intro"-------
    for thisComponent in RS_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('RS_intro_title.started', RS_intro_title.tStartRefresh)
    run.addData('RS_intro_title.stopped', RS_intro_title.tStopRefresh)
    run.addData('RS_intro_text.started', RS_intro_text.tStartRefresh)
    run.addData('RS_intro_text.stopped', RS_intro_text.tStopRefresh)
    RS_intro_audio_close.stop()  # ensure sound has stopped at end of routine
    run.addData('RS_intro_audio_close.started', RS_intro_audio_close.tStartRefresh)
    run.addData('RS_intro_audio_close.stopped', RS_intro_audio_close.tStopRefresh)
    run.addData('RS_intro_cont.started', RS_intro_cont.tStartRefresh)
    run.addData('RS_intro_cont.stopped', RS_intro_cont.tStopRefresh)
    # the Routine "RS_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RS_rec"-------
    # update component parameters for each repeat
    print("sending trigger 1")
    RS_rec_key_resp.keys = []
    RS_rec_key_resp.rt = []
    # keep track of which components have finished
    RS_recComponents = [RS_rec_text, RS_rec_key_resp, RS_rec_cont]
    for thisComponent in RS_recComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RS_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "RS_rec"-------
    while continueRoutine:
        # get current time
        t = RS_recClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RS_recClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RS_rec_text* updates
        if RS_rec_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RS_rec_text.frameNStart = frameN  # exact frame index
            RS_rec_text.tStart = t  # local t and not account for scr refresh
            RS_rec_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_rec_text, 'tStartRefresh')  # time at next scr refresh
            RS_rec_text.setAutoDraw(True)
        if RS_rec_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RS_rec_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                RS_rec_text.tStop = t  # not accounting for scr refresh
                RS_rec_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RS_rec_text, 'tStopRefresh')  # time at next scr refresh
                RS_rec_text.setAutoDraw(False)
        
        # *RS_rec_key_resp* updates
        waitOnFlip = False
        if RS_rec_key_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            RS_rec_key_resp.frameNStart = frameN  # exact frame index
            RS_rec_key_resp.tStart = t  # local t and not account for scr refresh
            RS_rec_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_rec_key_resp, 'tStartRefresh')  # time at next scr refresh
            RS_rec_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(RS_rec_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RS_rec_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = RS_rec_key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *RS_rec_cont* updates
        if RS_rec_cont.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            RS_rec_cont.frameNStart = frameN  # exact frame index
            RS_rec_cont.tStart = t  # local t and not account for scr refresh
            RS_rec_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RS_rec_cont, 'tStartRefresh')  # time at next scr refresh
            RS_rec_cont.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RS_recComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RS_rec"-------
    for thisComponent in RS_recComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('RS_rec_text.started', RS_rec_text.tStartRefresh)
    run.addData('RS_rec_text.stopped', RS_rec_text.tStopRefresh)
    print("sending trigger 0")
    run.addData('RS_rec_cont.started', RS_rec_cont.tStartRefresh)
    run.addData('RS_rec_cont.stopped', RS_rec_cont.tStopRefresh)
    # the Routine "RS_rec" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "QA_intro"-------
    # update component parameters for each repeat
    QA_intro_audio.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/q_a/q_a.wav', secs=32, hamming=True)
    QA_intro_audio.setVolume(1, log=False)
    QA_intro_key_resp.keys = []
    QA_intro_key_resp.rt = []
    # keep track of which components have finished
    QA_introComponents = [QA_intro_title, QA_intro_text, QA_intro_audio, QA_intro_key_resp, QA_intro_cont]
    for thisComponent in QA_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QA_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "QA_intro"-------
    while continueRoutine:
        # get current time
        t = QA_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QA_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *QA_intro_title* updates
        if QA_intro_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QA_intro_title.frameNStart = frameN  # exact frame index
            QA_intro_title.tStart = t  # local t and not account for scr refresh
            QA_intro_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QA_intro_title, 'tStartRefresh')  # time at next scr refresh
            QA_intro_title.setAutoDraw(True)
        if QA_intro_title.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > QA_intro_title.tStartRefresh + 32-frameTolerance:
                # keep track of stop time/frame for later
                QA_intro_title.tStop = t  # not accounting for scr refresh
                QA_intro_title.frameNStop = frameN  # exact frame index
                win.timeOnFlip(QA_intro_title, 'tStopRefresh')  # time at next scr refresh
                QA_intro_title.setAutoDraw(False)
        
        # *QA_intro_text* updates
        if QA_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QA_intro_text.frameNStart = frameN  # exact frame index
            QA_intro_text.tStart = t  # local t and not account for scr refresh
            QA_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QA_intro_text, 'tStartRefresh')  # time at next scr refresh
            QA_intro_text.setAutoDraw(True)
        if QA_intro_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > QA_intro_text.tStartRefresh + 32-frameTolerance:
                # keep track of stop time/frame for later
                QA_intro_text.tStop = t  # not accounting for scr refresh
                QA_intro_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(QA_intro_text, 'tStopRefresh')  # time at next scr refresh
                QA_intro_text.setAutoDraw(False)
        # start/stop QA_intro_audio
        if QA_intro_audio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            QA_intro_audio.frameNStart = frameN  # exact frame index
            QA_intro_audio.tStart = t  # local t and not account for scr refresh
            QA_intro_audio.tStartRefresh = tThisFlipGlobal  # on global time
            QA_intro_audio.play(when=win)  # sync with win flip
        if QA_intro_audio.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > QA_intro_audio.tStartRefresh + 32-frameTolerance:
                # keep track of stop time/frame for later
                QA_intro_audio.tStop = t  # not accounting for scr refresh
                QA_intro_audio.frameNStop = frameN  # exact frame index
                win.timeOnFlip(QA_intro_audio, 'tStopRefresh')  # time at next scr refresh
                QA_intro_audio.stop()
        
        # *QA_intro_key_resp* updates
        waitOnFlip = False
        if QA_intro_key_resp.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            QA_intro_key_resp.frameNStart = frameN  # exact frame index
            QA_intro_key_resp.tStart = t  # local t and not account for scr refresh
            QA_intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QA_intro_key_resp, 'tStartRefresh')  # time at next scr refresh
            QA_intro_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(QA_intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if QA_intro_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = QA_intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *QA_intro_cont* updates
        if QA_intro_cont.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            QA_intro_cont.frameNStart = frameN  # exact frame index
            QA_intro_cont.tStart = t  # local t and not account for scr refresh
            QA_intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QA_intro_cont, 'tStartRefresh')  # time at next scr refresh
            QA_intro_cont.setAutoDraw(True)
        if QA_intro_cont.status == STARTED:  # only update if drawing
            QA_intro_cont.setText('Press [space] key to continue.', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QA_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "QA_intro"-------
    for thisComponent in QA_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('QA_intro_title.started', QA_intro_title.tStartRefresh)
    run.addData('QA_intro_title.stopped', QA_intro_title.tStopRefresh)
    run.addData('QA_intro_text.started', QA_intro_text.tStartRefresh)
    run.addData('QA_intro_text.stopped', QA_intro_text.tStopRefresh)
    QA_intro_audio.stop()  # ensure sound has stopped at end of routine
    run.addData('QA_intro_audio.started', QA_intro_audio.tStartRefresh)
    run.addData('QA_intro_audio.stopped', QA_intro_audio.tStopRefresh)
    run.addData('QA_intro_cont.started', QA_intro_cont.tStartRefresh)
    run.addData('QA_intro_cont.stopped', QA_intro_cont.tStopRefresh)
    # the Routine "QA_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    QA_pre_block = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='QA_pre_block')
    thisExp.addLoop(QA_pre_block)  # add the loop to the experiment
    thisQA_pre_block = QA_pre_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQA_pre_block.rgb)
    if thisQA_pre_block != None:
        for paramName in thisQA_pre_block:
            exec('{} = thisQA_pre_block[paramName]'.format(paramName))
    
    for thisQA_pre_block in QA_pre_block:
        currentLoop = QA_pre_block
        # abbreviate parameter names if possible (e.g. rgb = thisQA_pre_block.rgb)
        if thisQA_pre_block != None:
            for paramName in thisQA_pre_block:
                exec('{} = thisQA_pre_block[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        pre_trial = data.TrialHandler(nReps=3, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='pre_trial')
        thisExp.addLoop(pre_trial)  # add the loop to the experiment
        thisPre_trial = pre_trial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPre_trial.rgb)
        if thisPre_trial != None:
            for paramName in thisPre_trial:
                exec('{} = thisPre_trial[paramName]'.format(paramName))
        
        for thisPre_trial in pre_trial:
            currentLoop = pre_trial
            # abbreviate parameter names if possible (e.g. rgb = thisPre_trial.rgb)
            if thisPre_trial != None:
                for paramName in thisPre_trial:
                    exec('{} = thisPre_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "QA_rec"-------
            routineTimer.add(30.000000)
            # update component parameters for each repeat
            QA_rec_beep_hint.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, hamming=True)
            QA_rec_beep_hint.setVolume(1, log=False)
            QA_rec_question.setSound('../../../../Data/NIBS/Stage_one/Audio/Database/article_0/sentence_0/sentence_0_syn.wav', secs=14.4, hamming=True)
            QA_rec_question.setVolume(1, log=False)
            QA_rec_beep_start.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, hamming=True)
            QA_rec_beep_start.setVolume(1, log=False)
            
            
            # Create a voice-key to be used:
            file_name ='data/rec_QA_pre_block_'+ str(QA_pre_block.thisN).zfill(3) + '_trial_' + str(pre_trial.thisN).zfill(3)  + '.wav'
            fs = 44100  # Sample rate
            seconds = 30  # Duration of recording
            
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            #  sd.wait()  # Wait until recording is finished
            
            QA_rec_beep_end.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, hamming=True)
            QA_rec_beep_end.setVolume(1, log=False)
            # keep track of which components have finished
            QA_recComponents = [QA_rec_text, QA_rec_beep_hint, QA_rec_question, QA_rec_beep_start, QA_rec_beep_end, QA_rec_break]
            for thisComponent in QA_recComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            QA_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "QA_rec"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = QA_recClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=QA_recClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *QA_rec_text* updates
                if QA_rec_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_text.frameNStart = frameN  # exact frame index
                    QA_rec_text.tStart = t  # local t and not account for scr refresh
                    QA_rec_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(QA_rec_text, 'tStartRefresh')  # time at next scr refresh
                    QA_rec_text.setAutoDraw(True)
                if QA_rec_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_text.tStartRefresh + 25-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_text.tStop = t  # not accounting for scr refresh
                        QA_rec_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_text, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_text.setAutoDraw(False)
                # start/stop QA_rec_beep_hint
                if QA_rec_beep_hint.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_beep_hint.frameNStart = frameN  # exact frame index
                    QA_rec_beep_hint.tStart = t  # local t and not account for scr refresh
                    QA_rec_beep_hint.tStartRefresh = tThisFlipGlobal  # on global time
                    QA_rec_beep_hint.play(when=win)  # sync with win flip
                if QA_rec_beep_hint.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_beep_hint.tStartRefresh + 0.6-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_beep_hint.tStop = t  # not accounting for scr refresh
                        QA_rec_beep_hint.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_beep_hint, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_beep_hint.stop()
                # start/stop QA_rec_question
                if QA_rec_question.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_question.frameNStart = frameN  # exact frame index
                    QA_rec_question.tStart = t  # local t and not account for scr refresh
                    QA_rec_question.tStartRefresh = tThisFlipGlobal  # on global time
                    QA_rec_question.play(when=win)  # sync with win flip
                if QA_rec_question.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_question.tStartRefresh + 14.4-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_question.tStop = t  # not accounting for scr refresh
                        QA_rec_question.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_question, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_question.stop()
                # start/stop QA_rec_beep_start
                if QA_rec_beep_start.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_beep_start.frameNStart = frameN  # exact frame index
                    QA_rec_beep_start.tStart = t  # local t and not account for scr refresh
                    QA_rec_beep_start.tStartRefresh = tThisFlipGlobal  # on global time
                    QA_rec_beep_start.play(when=win)  # sync with win flip
                if QA_rec_beep_start.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_beep_start.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_beep_start.tStop = t  # not accounting for scr refresh
                        QA_rec_beep_start.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_beep_start, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_beep_start.stop()
                # Nothing needed every frame for this demo
                # start/stop QA_rec_beep_end
                if QA_rec_beep_end.status == NOT_STARTED and tThisFlip >= 24-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_beep_end.frameNStart = frameN  # exact frame index
                    QA_rec_beep_end.tStart = t  # local t and not account for scr refresh
                    QA_rec_beep_end.tStartRefresh = tThisFlipGlobal  # on global time
                    QA_rec_beep_end.play(when=win)  # sync with win flip
                if QA_rec_beep_end.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_beep_end.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_beep_end.tStop = t  # not accounting for scr refresh
                        QA_rec_beep_end.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_beep_end, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_beep_end.stop()
                
                # *QA_rec_break* updates
                if QA_rec_break.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
                    # keep track of start time/frame for later
                    QA_rec_break.frameNStart = frameN  # exact frame index
                    QA_rec_break.tStart = t  # local t and not account for scr refresh
                    QA_rec_break.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(QA_rec_break, 'tStartRefresh')  # time at next scr refresh
                    QA_rec_break.setAutoDraw(True)
                if QA_rec_break.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QA_rec_break.tStartRefresh + 5.0-frameTolerance:
                        # keep track of stop time/frame for later
                        QA_rec_break.tStop = t  # not accounting for scr refresh
                        QA_rec_break.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QA_rec_break, 'tStopRefresh')  # time at next scr refresh
                        QA_rec_break.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in QA_recComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "QA_rec"-------
            for thisComponent in QA_recComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            pre_trial.addData('QA_rec_text.started', QA_rec_text.tStartRefresh)
            pre_trial.addData('QA_rec_text.stopped', QA_rec_text.tStopRefresh)
            QA_rec_beep_hint.stop()  # ensure sound has stopped at end of routine
            pre_trial.addData('QA_rec_beep_hint.started', QA_rec_beep_hint.tStartRefresh)
            pre_trial.addData('QA_rec_beep_hint.stopped', QA_rec_beep_hint.tStopRefresh)
            QA_rec_question.stop()  # ensure sound has stopped at end of routine
            pre_trial.addData('QA_rec_question.started', QA_rec_question.tStartRefresh)
            pre_trial.addData('QA_rec_question.stopped', QA_rec_question.tStopRefresh)
            QA_rec_beep_start.stop()  # ensure sound has stopped at end of routine
            pre_trial.addData('QA_rec_beep_start.started', QA_rec_beep_start.tStartRefresh)
            pre_trial.addData('QA_rec_beep_start.stopped', QA_rec_beep_start.tStopRefresh)
            
            write(file_name, fs, myrecording)  # Save as WAV file 
            # Add the detected time into the PsychoPy data file:
            # thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
            # thisExp.addData('bad_baseline', vpvk.bad_baseline)
            thisExp.addData('filename', file_name)
            thisExp.nextEntry()
            QA_rec_beep_end.stop()  # ensure sound has stopped at end of routine
            pre_trial.addData('QA_rec_beep_end.started', QA_rec_beep_end.tStartRefresh)
            pre_trial.addData('QA_rec_beep_end.stopped', QA_rec_beep_end.tStopRefresh)
            pre_trial.addData('QA_rec_break.started', QA_rec_break.tStartRefresh)
            pre_trial.addData('QA_rec_break.stopped', QA_rec_break.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 3 repeats of 'pre_trial'
        
        
        # ------Prepare to start Routine "Pause"-------
        # update component parameters for each repeat
        Pause_key_resp.keys = []
        Pause_key_resp.rt = []
        Pause_text.setText('Press [space] key to continue.')
        # keep track of which components have finished
        PauseComponents = [Pause_key_resp, Pause_text]
        for thisComponent in PauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Pause"-------
        while continueRoutine:
            # get current time
            t = PauseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PauseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Pause_key_resp* updates
            waitOnFlip = False
            if Pause_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pause_key_resp.frameNStart = frameN  # exact frame index
                Pause_key_resp.tStart = t  # local t and not account for scr refresh
                Pause_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pause_key_resp, 'tStartRefresh')  # time at next scr refresh
                Pause_key_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Pause_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Pause_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = Pause_key_resp.getKeys(keyList=['space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    # a response ends the routine
                    continueRoutine = False
            
            # *Pause_text* updates
            if Pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pause_text.frameNStart = frameN  # exact frame index
                Pause_text.tStart = t  # local t and not account for scr refresh
                Pause_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pause_text, 'tStartRefresh')  # time at next scr refresh
                Pause_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pause"-------
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        QA_pre_block.addData('Pause_text.started', Pause_text.tStartRefresh)
        QA_pre_block.addData('Pause_text.stopped', Pause_text.tStopRefresh)
        # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'QA_pre_block'
    
    thisExp.nextEntry()
    
# completed 3 repeats of 'run'


# ------Prepare to start Routine "Cali_de_post_intro"-------
# update component parameters for each repeat
Cali_de_post_intro_audio.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/cali_de.wav', secs=23, hamming=True)
Cali_de_post_intro_audio.setVolume(1, log=False)
Cali_de_post_intro_key_resp.keys = []
Cali_de_post_intro_key_resp.rt = []
# keep track of which components have finished
Cali_de_post_introComponents = [Cali_de_post_intro_title, Cali_de_post_intro_text, Cali_de_post_intro_audio, Cali_de_post_intro_key_resp, Cali_de_post_intro_cont]
for thisComponent in Cali_de_post_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Cali_de_post_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Cali_de_post_intro"-------
while continueRoutine:
    # get current time
    t = Cali_de_post_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Cali_de_post_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cali_de_post_intro_title* updates
    if Cali_de_post_intro_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_intro_title.frameNStart = frameN  # exact frame index
        Cali_de_post_intro_title.tStart = t  # local t and not account for scr refresh
        Cali_de_post_intro_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_intro_title, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_intro_title.setAutoDraw(True)
    if Cali_de_post_intro_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_intro_title.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_intro_title.tStop = t  # not accounting for scr refresh
            Cali_de_post_intro_title.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_intro_title, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_intro_title.setAutoDraw(False)
    
    # *Cali_de_post_intro_text* updates
    if Cali_de_post_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_intro_text.frameNStart = frameN  # exact frame index
        Cali_de_post_intro_text.tStart = t  # local t and not account for scr refresh
        Cali_de_post_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_intro_text, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_intro_text.setAutoDraw(True)
    if Cali_de_post_intro_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_intro_text.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_intro_text.tStop = t  # not accounting for scr refresh
            Cali_de_post_intro_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_intro_text, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_intro_text.setAutoDraw(False)
    # start/stop Cali_de_post_intro_audio
    if Cali_de_post_intro_audio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_intro_audio.frameNStart = frameN  # exact frame index
        Cali_de_post_intro_audio.tStart = t  # local t and not account for scr refresh
        Cali_de_post_intro_audio.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_post_intro_audio.play(when=win)  # sync with win flip
    if Cali_de_post_intro_audio.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_intro_audio.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_intro_audio.tStop = t  # not accounting for scr refresh
            Cali_de_post_intro_audio.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_intro_audio, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_intro_audio.stop()
    
    # *Cali_de_post_intro_key_resp* updates
    waitOnFlip = False
    if Cali_de_post_intro_key_resp.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_intro_key_resp.frameNStart = frameN  # exact frame index
        Cali_de_post_intro_key_resp.tStart = t  # local t and not account for scr refresh
        Cali_de_post_intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_intro_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Cali_de_post_intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Cali_de_post_intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Cali_de_post_intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Cali_de_post_intro_cont* updates
    if Cali_de_post_intro_cont.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_intro_cont.frameNStart = frameN  # exact frame index
        Cali_de_post_intro_cont.tStart = t  # local t and not account for scr refresh
        Cali_de_post_intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_intro_cont, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_intro_cont.setAutoDraw(True)
    if Cali_de_post_intro_cont.status == STARTED:  # only update if drawing
        Cali_de_post_intro_cont.setText('Press [space] key to continue.', log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cali_de_post_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cali_de_post_intro"-------
for thisComponent in Cali_de_post_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Cali_de_post_intro_title.started', Cali_de_post_intro_title.tStartRefresh)
thisExp.addData('Cali_de_post_intro_title.stopped', Cali_de_post_intro_title.tStopRefresh)
thisExp.addData('Cali_de_post_intro_text.started', Cali_de_post_intro_text.tStartRefresh)
thisExp.addData('Cali_de_post_intro_text.stopped', Cali_de_post_intro_text.tStopRefresh)
Cali_de_post_intro_audio.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_post_intro_audio.started', Cali_de_post_intro_audio.tStartRefresh)
thisExp.addData('Cali_de_post_intro_audio.stopped', Cali_de_post_intro_audio.tStopRefresh)
thisExp.addData('Cali_de_post_intro_cont.started', Cali_de_post_intro_cont.tStartRefresh)
thisExp.addData('Cali_de_post_intro_cont.stopped', Cali_de_post_intro_cont.tStopRefresh)
# the Routine "Cali_de_post_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cali_de_post_rec"-------
# update component parameters for each repeat
Cali_de_post_rec_beep_hint.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C5_A_tone_flat_half_s.wav', secs=0.6, hamming=True)
Cali_de_post_rec_beep_hint.setVolume(1, log=False)
Cali_de_post_rec_beep_start.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s.wav', secs=1, hamming=True)
Cali_de_post_rec_beep_start.setVolume(1, log=False)


# Create a voice-key to be used:
file_name ='data/rec_cali_de_pre.wav'
fs = 44100  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#  sd.wait()  # Wait until recording is finished

Cali_de_post_rec_beep_end.setSound('../../../../Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s.wav', secs=1, hamming=True)
Cali_de_post_rec_beep_end.setVolume(1, log=False)
Cali_de_post_rec_key_resp.keys = []
Cali_de_post_rec_key_resp.rt = []
# keep track of which components have finished
Cali_de_post_recComponents = [Cali_de_post_rec_text, Cali_de_post_rec_beep_hint, Cali_de_post_rec_beep_start, Cali_de_post_rec_beep_end, Cali_de_post_rec_key_resp, Cali_de_post_rec_cont]
for thisComponent in Cali_de_post_recComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Cali_de_post_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Cali_de_post_rec"-------
while continueRoutine:
    # get current time
    t = Cali_de_post_recClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Cali_de_post_recClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cali_de_post_rec_text* updates
    if Cali_de_post_rec_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_text.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_text.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_rec_text, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_rec_text.setAutoDraw(True)
    if Cali_de_post_rec_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_rec_text.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_rec_text.tStop = t  # not accounting for scr refresh
            Cali_de_post_rec_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_rec_text, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_rec_text.setAutoDraw(False)
    # start/stop Cali_de_post_rec_beep_hint
    if Cali_de_post_rec_beep_hint.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_beep_hint.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_beep_hint.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_beep_hint.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_post_rec_beep_hint.play(when=win)  # sync with win flip
    if Cali_de_post_rec_beep_hint.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_rec_beep_hint.tStartRefresh + 0.6-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_rec_beep_hint.tStop = t  # not accounting for scr refresh
            Cali_de_post_rec_beep_hint.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_rec_beep_hint, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_rec_beep_hint.stop()
    # start/stop Cali_de_post_rec_beep_start
    if Cali_de_post_rec_beep_start.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_beep_start.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_beep_start.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_beep_start.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_post_rec_beep_start.play(when=win)  # sync with win flip
    if Cali_de_post_rec_beep_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_rec_beep_start.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_rec_beep_start.tStop = t  # not accounting for scr refresh
            Cali_de_post_rec_beep_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_rec_beep_start, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_rec_beep_start.stop()
    # Nothing needed every frame for this demo
    # start/stop Cali_de_post_rec_beep_end
    if Cali_de_post_rec_beep_end.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_beep_end.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_beep_end.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_beep_end.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_post_rec_beep_end.play(when=win)  # sync with win flip
    if Cali_de_post_rec_beep_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_post_rec_beep_end.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_post_rec_beep_end.tStop = t  # not accounting for scr refresh
            Cali_de_post_rec_beep_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_post_rec_beep_end, 'tStopRefresh')  # time at next scr refresh
            Cali_de_post_rec_beep_end.stop()
    
    # *Cali_de_post_rec_key_resp* updates
    waitOnFlip = False
    if Cali_de_post_rec_key_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_key_resp.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_key_resp.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_rec_key_resp, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_rec_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Cali_de_post_rec_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Cali_de_post_rec_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Cali_de_post_rec_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Cali_de_post_rec_cont* updates
    if Cali_de_post_rec_cont.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_post_rec_cont.frameNStart = frameN  # exact frame index
        Cali_de_post_rec_cont.tStart = t  # local t and not account for scr refresh
        Cali_de_post_rec_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_post_rec_cont, 'tStartRefresh')  # time at next scr refresh
        Cali_de_post_rec_cont.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Cali_de_post_recComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Cali_de_post_rec"-------
for thisComponent in Cali_de_post_recComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Cali_de_post_rec_text.started', Cali_de_post_rec_text.tStartRefresh)
thisExp.addData('Cali_de_post_rec_text.stopped', Cali_de_post_rec_text.tStopRefresh)
Cali_de_post_rec_beep_hint.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_post_rec_beep_hint.started', Cali_de_post_rec_beep_hint.tStartRefresh)
thisExp.addData('Cali_de_post_rec_beep_hint.stopped', Cali_de_post_rec_beep_hint.tStopRefresh)
Cali_de_post_rec_beep_start.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_post_rec_beep_start.started', Cali_de_post_rec_beep_start.tStartRefresh)
thisExp.addData('Cali_de_post_rec_beep_start.stopped', Cali_de_post_rec_beep_start.tStopRefresh)

write(file_name, fs, myrecording)  # Save as WAV file 
# Add the detected time into the PsychoPy data file:
# thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
# thisExp.addData('bad_baseline', vpvk.bad_baseline)
thisExp.addData('filename', file_name)
thisExp.nextEntry()
Cali_de_post_rec_beep_end.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_post_rec_beep_end.started', Cali_de_post_rec_beep_end.tStartRefresh)
thisExp.addData('Cali_de_post_rec_beep_end.stopped', Cali_de_post_rec_beep_end.tStopRefresh)
thisExp.addData('Cali_de_post_rec_cont.started', Cali_de_post_rec_cont.tStartRefresh)
thisExp.addData('Cali_de_post_rec_cont.stopped', Cali_de_post_rec_cont.tStopRefresh)
# the Routine "Cali_de_post_rec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "the_end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
the_endComponents = [text_3]
for thisComponent in the_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
the_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "the_end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = the_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=the_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "the_end"-------
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

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
