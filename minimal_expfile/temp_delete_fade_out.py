
event_dict = {'ESC': 1,
              'Test': 253,
              'Main': 254,
              'End':255,
              'Pre_run': [2, 3],
              'Post_run': [8, 9],
              'Run': [4, 5],
              'Block': [6, 7],
              'Cali_intro': [10, 11],
              'Cali_trial': [12, 13],
              'Cali_display': [14, 15],
              'Cali_ans': [16, 17],
              'Cali_rec': [18, 19],
              'Stim': [20, 21],
              'Sham': [22, 23],
              'Fade_in': [24, 25],
              'Fade_out': [26, 27],
              'Stable_stim': [28, 29],
              'RS_intro': [30, 31],
              'RS_open': [32, 33],
              'RS_close': [34, 35],
              'QA_intro': [40, 41],
              'QA_trial': [42, 43],
              'QA_audio': [44, 45],
              'QA_ans': [46, 47],
              'QA_rec': [48, 49],
              'QA_cen_word': [50, 51],
              'Pause': [60, 61],
              'Break': [62, 63]}
    if fade_out_flag:
        print('Log: fade out start: Run ' + str(run.thisN))
        trigger_sending(event_dict['Stable_stim'][1], default_sleep=True) # Sending trigger 29 (Stable_stim End)

        time.sleep(60.000)
        if stim_freq == 0:

            win.flip()
            time.sleep(60.000)
            if run.thisN == stim_run[-1]:
                trigger_sending(event_dict['Sham'][1], default_sleep=True) # Sending trigger 23 (Sham End)
        else:
            if run.thisN == stim_run[-1]:
                # ------Prepare to start Routine "fade_in"-------
                
                # keep track of which components have finished
                win, fade_in, fade_inComponents, t, frameN, continueRoutine = pre_run_comp(win, fade_in)
                trigger_mat = np.zeros((len(fade_inComponents) - 1, 2))
                comp_list = np.asarray([*fade_in['time'].keys()])
                # trigger_encoding_sending('fade_in', input_run=0, input_block=0, intro_rec=0, input_event=0)
                stim_continue = False
                trigger_sending(event_dict['Fade_out'][0], default_sleep=True) # Sending trigger 26 (Fade_out Start)
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
                        fade_in['text'].setText('Please remain seated until further notice via the earphone.')
                    

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

                trigger_sending(event_dict['Fade_out'][1], default_sleep=True) # Sending trigger 27 (Fade_out End)
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


                trigger_sending(event_dict['Stim'][1], default_sleep=True) # Sending trigger 21 (Stim End)
            else:
                win.flip()
                time.sleep(30.000)
            routineTimer.reset()
        print('Log: fade out finish: Run ' + str(run.thisN))