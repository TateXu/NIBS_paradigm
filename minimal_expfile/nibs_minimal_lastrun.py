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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'nibs_stage_1'  # from the Builder filename that created this script
expInfo = {'participant': '001', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='nibs_minimal_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()

# The import and pyo_init should always come early on:
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=32)

# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler

# To use a LabJack as a signaling device:
#from voicekey.signal.labjack_vks import LabJackU3VoiceKeySignal as Signaler
import ctypes



import sounddevice as sd
from scipy.io.wavfile import write
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text='Welcome to participate our experiment: causal prediction model for non-invasive brain stimulation\n\nTask introductrion: \n\n',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_instruction = keyboard.Keyboard()
cont_instruction = visual.TextStim(win=win, name='cont_instruction',
    text='Press [space] key to continue.',
    font='Arial',
    pos=[0.5, -0.3], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Cali_de_pre_intro"
Cali_de_pre_introClock = core.Clock()
Cali_de_pre_intro_title = visual.TextStim(win=win, name='Cali_de_pre_intro_title',
    text='READ OUT BLOCK (GERMAN)',
    font='Arial',
    pos=[0.5, 0.5], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cali_de_pre_intro_text = visual.TextStim(win=win, name='Cali_de_pre_intro_text',
    text='1. Several sentences written in German on the screen, and please read out them loudly after hearing an increasing tonal beeping sound.\n2. A decreasing tonal beeping sound indicates the recording is finished.',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Cali_de_pre_intro_audio = sound.Sound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/cali_de_new.wav', secs=-1, stereo=True, hamming=True,
    name='Cali_de_pre_intro_audio')
Cali_de_pre_intro_audio.setVolume(1)
Cali_de_pre_intro_key_resp = keyboard.Keyboard()
Cali_de_pre_intro_cont = visual.TextStim(win=win, name='Cali_de_pre_intro_cont',
    text='default text',
    font='Arial',
    pos=[0.5, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Cali_de_pre_rec"
Cali_de_pre_recClock = core.Clock()
Cali_de_pre_rec_text = visual.TextStim(win=win, name='Cali_de_pre_rec_text',
    text='Hallo, Ich bin Chen aus Wien.',
    font='Arial',
    pos=(0.5, 0.2), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cali_de_pre_rec_beep_hint = sound.Sound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/reminder.wav', secs=0.6, stereo=True, hamming=True,
    name='Cali_de_pre_rec_beep_hint')
Cali_de_pre_rec_beep_hint.setVolume(1)
Cali_de_pre_rec_beep_start = sound.Sound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s_new.wav', secs=1, stereo=True, hamming=True,
    name='Cali_de_pre_rec_beep_start')
Cali_de_pre_rec_beep_start.setVolume(1)
Cali_de_pre_rec_beep_end = sound.Sound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s_new.wav', secs=1, stereo=True, hamming=True,
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

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
key_resp_instruction.keys = []
key_resp_instruction.rt = []
# keep track of which components have finished
InstructionsComponents = [instruction_text, key_resp_instruction, cont_instruction]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)
    
    # *key_resp_instruction* updates
    waitOnFlip = False
    if key_resp_instruction.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruction.frameNStart = frameN  # exact frame index
        key_resp_instruction.tStart = t  # local t and not account for scr refresh
        key_resp_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruction, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruction.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruction.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *cont_instruction* updates
    if cont_instruction.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        cont_instruction.frameNStart = frameN  # exact frame index
        cont_instruction.tStart = t  # local t and not account for scr refresh
        cont_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_instruction, 'tStartRefresh')  # time at next scr refresh
        cont_instruction.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text.started', instruction_text.tStartRefresh)
thisExp.addData('instruction_text.stopped', instruction_text.tStopRefresh)
thisExp.addData('cont_instruction.started', cont_instruction.tStartRefresh)
thisExp.addData('cont_instruction.stopped', cont_instruction.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cali_de_pre_intro"-------
# update component parameters for each repeat
Cali_de_pre_intro_audio.setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/cali_de_new.wav', secs=23, hamming=True)
Cali_de_pre_intro_audio.setVolume(1, log=False)
Cali_de_pre_intro_key_resp.keys = []
Cali_de_pre_intro_key_resp.rt = []
# keep track of which components have finished
Cali_de_pre_introComponents = [Cali_de_pre_intro_title, Cali_de_pre_intro_text, Cali_de_pre_intro_audio, Cali_de_pre_intro_key_resp, Cali_de_pre_intro_cont]
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
Cali_de_pre_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Cali_de_pre_intro"-------
while continueRoutine:
    # get current time
    t = Cali_de_pre_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Cali_de_pre_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cali_de_pre_intro_title* updates
    if Cali_de_pre_intro_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro_title.frameNStart = frameN  # exact frame index
        Cali_de_pre_intro_title.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro_title, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro_title.setAutoDraw(True)
    if Cali_de_pre_intro_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro_title.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro_title.tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro_title.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro_title, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro_title.setAutoDraw(False)
    
    # *Cali_de_pre_intro_text* updates
    if Cali_de_pre_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro_text.frameNStart = frameN  # exact frame index
        Cali_de_pre_intro_text.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro_text, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro_text.setAutoDraw(True)
    if Cali_de_pre_intro_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro_text.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro_text.tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro_text, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro_text.setAutoDraw(False)
    # start/stop Cali_de_pre_intro_audio
    if Cali_de_pre_intro_audio.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro_audio.frameNStart = frameN  # exact frame index
        Cali_de_pre_intro_audio.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro_audio.tStartRefresh = tThisFlipGlobal  # on global time
        Cali_de_pre_intro_audio.play(when=win)  # sync with win flip
    if Cali_de_pre_intro_audio.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cali_de_pre_intro_audio.tStartRefresh + 23-frameTolerance:
            # keep track of stop time/frame for later
            Cali_de_pre_intro_audio.tStop = t  # not accounting for scr refresh
            Cali_de_pre_intro_audio.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cali_de_pre_intro_audio, 'tStopRefresh')  # time at next scr refresh
            Cali_de_pre_intro_audio.stop()
    
    # *Cali_de_pre_intro_key_resp* updates
    waitOnFlip = False
    if Cali_de_pre_intro_key_resp.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro_key_resp.frameNStart = frameN  # exact frame index
        Cali_de_pre_intro_key_resp.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Cali_de_pre_intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Cali_de_pre_intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Cali_de_pre_intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *Cali_de_pre_intro_cont* updates
    if Cali_de_pre_intro_cont.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        Cali_de_pre_intro_cont.frameNStart = frameN  # exact frame index
        Cali_de_pre_intro_cont.tStart = t  # local t and not account for scr refresh
        Cali_de_pre_intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cali_de_pre_intro_cont, 'tStartRefresh')  # time at next scr refresh
        Cali_de_pre_intro_cont.setAutoDraw(True)
    if Cali_de_pre_intro_cont.status == STARTED:  # only update if drawing
        Cali_de_pre_intro_cont.setText('Press [space] key to continue.', log=False)
    
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
thisExp.addData('Cali_de_pre_intro_title.started', Cali_de_pre_intro_title.tStartRefresh)
thisExp.addData('Cali_de_pre_intro_title.stopped', Cali_de_pre_intro_title.tStopRefresh)
thisExp.addData('Cali_de_pre_intro_text.started', Cali_de_pre_intro_text.tStartRefresh)
thisExp.addData('Cali_de_pre_intro_text.stopped', Cali_de_pre_intro_text.tStopRefresh)
Cali_de_pre_intro_audio.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Cali_de_pre_intro_audio.started', Cali_de_pre_intro_audio.tStartRefresh)
thisExp.addData('Cali_de_pre_intro_audio.stopped', Cali_de_pre_intro_audio.tStopRefresh)
thisExp.addData('Cali_de_pre_intro_cont.started', Cali_de_pre_intro_cont.tStartRefresh)
thisExp.addData('Cali_de_pre_intro_cont.stopped', Cali_de_pre_intro_cont.tStopRefresh)
# the Routine "Cali_de_pre_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Cali_de_pre_rec"-------
# update component parameters for each repeat
Cali_de_pre_rec_beep_hint.setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/reminder.wav', secs=0.6, hamming=True)
Cali_de_pre_rec_beep_hint.setVolume(1, log=False)
Cali_de_pre_rec_beep_start.setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C3A_C4A_tone_decrease_1s_new.wav', secs=1, hamming=True)
Cali_de_pre_rec_beep_start.setVolume(1, log=False)


# Create a voice-key to be used:
file_name ='data/rec_cali_de_pre.wav'
fs = 44100  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#  sd.wait()  # Wait until recording is finished

Cali_de_pre_rec_beep_end.setSound('/home/jxu/File/Data/NIBS/Stage_one/Audio/Soundeffect/calibration/C4A_C3A_tone_decrease_1s_new.wav', secs=1, hamming=True)
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


# completed 3 repeats of 'run'


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
