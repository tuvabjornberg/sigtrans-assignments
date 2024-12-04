import numpy as np
import scipy
import matplotlib as plt
import sounddevice as sd
import time


t = [0, 5]
Ts = 0.1e-3
fs = 1 / Ts

tk = np.arange(t[0], t[1], Ts)

xk = np.sin(2000 * np.pi * tk)

sd.play(xk, fs, blocking=True)
time.sleep(2)

sd.stop()
