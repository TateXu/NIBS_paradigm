from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
from psychopy.sound import Sound


win = visual.Window([600,400], color='black', fullscr=0)
no_response = True
s = Sound(value=300, secs=2.0, volume=.03)
win.flip()
s.play()
timer = core.CountdownTimer(10000)

while timer.getTime() > 0 and no_response:
	timee = timer.getTime()
	for key in event.getKeys():
		if key in ['1', '2']:
			no_response = False
win.flip()
win.close()
core.quit()