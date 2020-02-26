
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
# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler
import sounddevice as sd
from scipy.io.wavfile import write
import parallel
import numbers
import pandas as pd


def exp_init():
    # -----------------------------------------------------------------------------------
    # -------------------- Experiment & Device initialization ---------------------------
    # -----------------------------------------------------------------------------------
    # Store info about the experiment session
    expName = 'nibs_stage_1'  # from the Builder filename that created this script
    Info = {'participant': '01', 'session': '01', 'First language':'', 'German level':''}
    dlg = gui.DlgFromDict(dictionary=Info, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    Info['date'] = data.getDateStr()  # add a simple timestamp
    Info['expName'] = expName
    Info['psychopyVersion'] = '3.2.3'

    # Setup the Window
    win = visual.Window(
        size=[960, 540], fullscr=False, screen=0, 
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

def path_init(expInfo):
    # -----------------------------------------------------------------------------------
    # ----------------------- Folder & File initialization ------------------------------
    # -----------------------------------------------------------------------------------
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)

    folder_path = './data/Subject_%s/Session_%s/Exp_data/' %(
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
    elif comp['property'] == 'recording':
        class rec: pass
        rec.status = None
        rec.name = routine + '_' + comp['comp_name']
        for k, v in comp['parameters'].items():
            setattr(rec, k, v)
        return rec
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
        'parameters':{'value': loc,
                      'volume':vol,
                      'sampleRate': sr,
                      'stereo': stereo,
                      'hamming': hamming,
                      'secs': secs}
        }
    return dict_audio


def rec_generator(name, sps=44100, n_rec_chn=2, loc='./data/'):
    dict_rec = {
        'property':'recording',
        'comp_name': name,
        'parameters':{'fs': sps,
                      'file_path': loc,
                      'channels': n_rec_chn,
                      'samplerate': sps}
        }
    return dict_rec


# keep track of which components have finished
def pre_run_comp(win, obj):
    objComponents = [v for v in obj.values() if not isinstance(v, dict)]
    for thisComponent in objComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    obj['clock'].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True

    return win, obj, objComponents, t, frameN, continueRoutine


def time_update(obj_clock, win, frame):
    current_time = obj_clock.getTime()
    current_routine_time = win.getFutureFlipTime(clock=obj_clock)
    current_global_time = win.getFutureFlipTime(clock=None)
    current_frame = frame + 1

    return current_frame, current_time, current_routine_time, current_global_time, win


def run_comp(win, obj, obj_property, current_frame, current_time, current_routine_time,
    current_global_time, start_time=0, duration=None, repeat_per_frame=False,
    repeat_content=None, frameTolerance=0.001, waitOnFlip=False, key_list=['space'],
    continueRoutine_flag=True, endExpNow_flag=False, fs=44100, rec_filepath=None, stim=False,
    stim_obj=None, stim_step_intensity=None, stim_current_intensity=None,
    stim_freq=None, stim_offset=None, stim_intensity_limit=None, stim_continue_flag=False):

    trigger_flag = False
    trigger_val = None
    if obj.status == NOT_STARTED and current_routine_time >= start_time-frameTolerance:
        # keep track of start time/frame for later
        obj.frameNStart = current_frame  # exact frame index
        obj.tStart = current_time  # local t and not account for scr refresh
        obj.tStartRefresh = current_global_time  # on global time
        trigger_flag = True 
        trigger_val = 1
        if obj_property == 'text':
            win.timeOnFlip(obj, 'tStartRefresh')  # time at next scr refresh
            obj.setAutoDraw(True)
        elif obj_property == 'audio':
            obj.play(when=win)  # sync with win flip
        elif obj_property == 'key_resp' or obj_property == 'key_resp_stim' :
            obj.status = STARTED
            win.callOnFlip(obj.clearEvents, eventType='keyboard')  # clear events on next screen flip
        elif obj_property == 'recording':
            obj.status = STARTED
            try:
                print('Recording start!')
                obj.file = sd.rec(int(duration * obj.fs), samplerate=obj.fs, channels=obj.channels)
            except:
                obj.file = None
                print('No predefined duration of recording!')
    
    if obj.status == STARTED:
        if repeat_per_frame or duration != None:
            if duration != None and current_global_time > obj.tStartRefresh + duration - frameTolerance:
                obj.tStop = current_time
                obj.frameNStop = current_frame
                win.timeOnFlip(obj, 'tStopRefresh')
                trigger_flag = True
                trigger_val = 0
                if obj_property == 'text':
                    obj.setAutoDraw(False)
                elif obj_property == 'audio':
                    obj.stop()
                elif obj_property == 'recording':
                    obj.status = FINISHED
            elif repeat_per_frame:
                if obj_property == 'text':
                    obj.setText(repeat_content, log=False)
                elif obj_property == 'audio':
                    pass
        if obj_property == 'key_resp' and not waitOnFlip:
            theseKeys = obj.getKeys(keyList=key_list, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow_flag = True
                else:
                    endExpNow_flag = False
                continueRoutine_flag = False

        if obj_property == 'key_resp_stim' and not waitOnFlip and stim:
            theseKeys = obj.getKeys(keyList=key_list, waitRelease=False)
            stim_min_intensity, stim_full_intensity = stim_intensity_limit
            stim_continue_flag = stim_continue_flag
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow_flag = True
                elif "space" == theseKeys:
                    stim_continue_flag = True
                elif "i" == theseKeys:
                    stim_current_intensity += stim_step_intensity
                elif "d" == theseKeys:
                    stim_current_intensity -= stim_step_intensity
                else:
                    endExpNow_flag = False

                if stim_current_intensity > stim_full_intensity:
                    stim_current_intensity = stim_full_intensity
                elif stim_current_intensity < stim_min_intensity:
                    stim_current_intensity = stim_min_intensity  # Minimum output of waveform generator
                else:
                    stim_current_intensity = stim_current_intensity

                stim_current_intensity = np.round(stim_current_intensity, 2)
                stim_obj.amp(stim_current_intensity)

                print(stim_current_intensity)
                if stim_freq is not None:
                    stim_obj.frequency(stim_freq)
                if stim_offset is not None:
                    stim_obj.offset(stim_offset)

                continueRoutine_flag = False

    if obj_property == 'key_resp':
        return win, obj, continueRoutine_flag, endExpNow_flag, np.asarray([[trigger_flag, trigger_val]])
    elif obj_property == 'key_resp_stim':
        return win, obj, stim_current_intensity, stim_continue_flag, continueRoutine_flag, endExpNow_flag, np.asarray([[trigger_flag, trigger_val]])
    else:
        return win, obj, np.asarray([[trigger_flag, trigger_val]])


def continue_justification(win, endExpNow_flag, defaultKeyboard, continueRoutine_flag, objComponents,
    break_flag=False):
    # check for quit (typically the Esc key)
    if endExpNow_flag or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine_flag:  # a component has requested a forced-end of Routine
        break_flag = True
    continueRoutine_flag = False  # will revert to True if at least one component still running
    for thisComponent in objComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine_flag = True
            break   # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine_flag:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

    return win, continueRoutine_flag, break_flag


def data_writer(target, obj, obj_str, list_kwgs):
    for kwgs in list_kwgs:
        if 'audio' in kwgs or 'beep' in kwgs or kwgs == 'question':
            obj[kwgs].stop() # ensure sound has stopped at end of routine
        target.addData(obj_str + '_' + kwgs + '.started', obj[kwgs].tStartRefresh)
        target.addData(obj_str + '_' + kwgs + '.stopped', obj[kwgs].tStopRefresh)
    return target


def trigger_sending(data, port):
    value = np.uint8(data)
    try: 
        ext_port = parallel.Parallel(port=port)
        ext_port.setData(value)
        return print('successfully send trigger: ' + value)
    except:
        return print('No device! Planned to send trigger: ' + value)


def trigger_encoding_sending(obj_name, input_run, input_block, intro_rec, input_event, port='/dev/parport0'):

    """
    0. Structure of Experiment
    =====================================================================================================
    | ------------- HEADER -------------- | ----------------------- DATA ------------------- | -FOOTER- |
    | START Exp. | Instruction | Practice | Pre-Run | Run 0 | Run 1 | ... | Run 3 | Post-Run | END Exp. |
    =====================================================================================================


    1.1. Structure of Pre-/Post-Run (Calibration)
    ===================================================================================
    |  -HEADER- | <--- 30 secs ---> | ........................... | ----- FOOTER ---- |
    |   Intro   |     C-Trial 0     | C-Trial 1 | ... | C-Tiral 9 | Pause (unlimited) |
    | < 1 min > | <------------------- 5 mins ------------------> | <----- n/a -----> |
    ===================================================================================

   
    1.2. Structure of Pre-/Post-Run trial (Calibration)
    =========================================================================================
    | ------------------------------ Calibration Trail K ---------------------------------- |
    | -------------------------------------- DATA ----------------------------------------- |
    |  Q-Beep | Display sentence | Blank |  A-S-Beep |    A-Rec   |  A-S-Beep | -- Break -- |
    | <----------- 18 secs ------------> | < 1 sec > | < 8 secs > | < 1 sec > | < 2 secs  > |
    =========================================================================================


    2.1. Structure of Run
    ===========================================================================================================
    | ----------------------------------------------- Run K ------------------------------------------------- |
    | ------------------------------------------------------------------------------------------------------- |
    | <--- 1 min ---> | <-- 10mins --> | <-- ~12mins --> | <-- 10mins --> | <-- ~12mins --> | <--- 1 min ---> |
    | START Stim/Sham | Resting State  |     Block 0     | Resting State  |     Block 1     |  END Stim/Sham  |
    | <--- 1 min ---> | <---------------------------- ~45mins ----------------------------> | <--- 1 min ---> |
    ===========================================================================================================


    2.1.1. Structure of Resting State
    ======================================================================
    | ------------------------- Resting State -------------------------- |
    | -- HEADER -- | ---------------- ------DATA ----------------------- |
    |    Intro     | Relax while opening eyes | Relax while closing eyes |
    | < 30 secs >  | <------- 5 mins -------> | <------- 5 mins -------> | 
    ======================================================================


    2.1.2. Structure of Block
    ==============================================================================
    | ---------------------------------- Block K ------------------------------- |
    |  -HEADER- | <-- 30 secs --> | ........................ | ----- FOOTER ---- |
    |   Intro   |     Trial 0     | Trial 1 | ... | Tiral 19 | Pause (unlimited) |
    | < 1 min > | <---------------- 10 mins ---------------> | <----- n/a -----> |
    ==============================================================================


    2.1.3. Structure of Trial (Q&A)
    ======================================================================================================================
    | ------------------------------------------------- Trial K -------------------------------------------------------- |
    | -Beep- | --------------- Question Audio--------------- -------- | --------- Answer Recording ------- | ----------- |
    | Q-Beep | Q-Audio-1 | Word censored by 40Hz |  Q-Audio-2 | Blank |  A-S-Beep |    A-Rec   |  A-S-Beep | -- Break -- |
    | <---------------------- 18 secs ------------------------------> | < 1 sec > | < 8 secs > | < 1 sec > | < 2 secs  > |
    ======================================================================================================================
    
    =============================
    |--- General Trigger (0) ---|
    =============================
    Pre-run   start/end: 0/1
    Post-Run  start/end: 2/3
    Run       start/end: 4/5
    Block     start/end: 6/7
    # Trial     start/end: 8/9
    
    ========================================
    |--- Calibration Trial Trigger (10) ---|
    ========================================
    Intro             start/end: 0/1
    Trial             start/end: 2/3
    Display           start/end: 4/5
    Answer            start/end: 6/7
    Answer recording  start/end: 8/9

    =================================
    |--- Stim./Sham Trigger (20) ---|
    =================================
    Stim.         start/end: 0/1
    Sham          start/end: 2/3
    Fade in       start/end: 4/5
    Fade out      start/end: 6/7
    Stable stim.  start/end: 8/9


    ====================================
    |--- Resting State Trigger (30) ---|
    ====================================
    Intro                start/end: 0/1
    Opening eyes         start/end: 2/3
    Closing eyes         start/end: 4/5


    ==========================================  
    |--- Q&A Block& Trial Trigger (40) ---|
    ==========================================
    Intro             start/end: 0/1
    Trial             start/end: 2/3
    Q-audio           start/end: 4/5
    Censored word     start/end: 6/7
    Answer            start/end: 8/9
    Answer recording  start/end: 10/11


    ===================================
    |---  Break/Pause Trigger (60) ---|
    ===================================
    Pause  start/end: 0/1
    Break  start/end: 2/3 
    


    """


    task = {'instruction': '0', 'Calibration': '1', 'RS': '2', 'QA': '3'}

    digit_task = task[obj_name]
    digit_run = str(input_run)
    digit_block = str(input_block)
    digit_intro_rec = str(intro_rec)

    if isinstance(input_event, numbers.Number):
        digit_event = str(input_event)
        data = digit_task + digit_run + digit_block + digit_intro_rec + digit_event
        trigger_sending(data, port=port)
    else:
        for ind in np.where(input_event[:, 0] == 1)[0]:
            digit_event = str(int(ind)) + str(int(input_event[ind, 1]))
            data = digit_task + digit_run + digit_block + digit_intro_rec + digit_event
            trigger_sending(data, port=port)


def extract_qa(input_all_df=None, type='train', subject=0, session=1, word_type='VB', n_question=3,
    file_root='/home/jxu/File/Data/NIBS/Stage_one/Audio/Database/'):
    
    if input_all_df == None: 
        dataframe_path = file_root + 'all_beep_df.pkl'
        all_df = pd.read_pickle(dataframe_path)
    else:
        all_df = input_all_df
    # No repeat questions for same subject
    # all_df['META_INFO']['tag_list'].str.len()
    no_repeat_df = all_df[all_df['EXP_INFO']['S' + str(subject).zfill(2)].isnull()]
    word_type_df = no_repeat_df[no_repeat_df['SENTENCE_INFO']['beep_word_type'] == word_type]
    
    # col_name = [('SENTENCE_INFO', 'article_id'), ('SENTENCE_INFO', 'sen_id'), ('SENTENCE_INFO', 'beeped_word'), ('META_INFO', 'audio_rate'), ('META_INFO', 'pitch')]
    col_name = [('SENTENCE_INFO', 'article_id'), ('SENTENCE_INFO', 'sen_id'), ('META_INFO', 'audio_rate'), ('META_INFO', 'pitch')]
    unique_sen_df = word_type_df.drop_duplicates(subset=col_name, keep='first')


    from numpy.random import default_rng
    import pdb
    pdb.set_trace()
    numbers = default_rng().choice(len(unique_sen_df.index), size=n_question, replace=False)
    randomize_indices = unique_sen_df.index[np.sort(numbers)]
    extract_df = unique_sen_df.loc[randomize_indices]
    file_loc_list = extract_df['PATH']['file_root_syn'].values

    for ind, value in enumerate(randomize_indices):
        all_df.at[value,('EXP_INFO','S' + str(subject).zfill(2))] = session
    print('Following indices are going to be set as question:')
    print(randomize_indices.values)
    all_df.to_pickle(dataframe_path)

    return extract_df, file_loc_list


