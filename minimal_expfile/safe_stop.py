from jxu.hardware.signal import SignalGenerator as SG 
import time
import numpy as np


fg = SG()

for i in [0.4, 0.3, 0.2, 0.1, 0.002]:
    fg.amp(i)
    time.sleep(6)
fg.off()