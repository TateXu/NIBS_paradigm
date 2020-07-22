from jxu.hardware.signal import SignalGenerator as SG 
import time
import numpy as np


fg = SG()
fg.on()
fg.frequency(40.0)
for i in [ 0.002, 0.1, 0.2, 0.3, 0.4, 0.5]:
    fg.amp(i)
    time.sleep(6)
