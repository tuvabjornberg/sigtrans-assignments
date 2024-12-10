import numpy as np
import scipy
import matplotlib.pyplot as plt
import sounddevice as sd
import time


t = [0, 5]
# a)
Ts = 0.5e-3
fs = 1 / Ts

# Ts = 1/fs
# fs = 2000


# b)
# fs = 1100
# Ts = 1 / fs

tk = np.arange(t[0], t[1], Ts)

xk = np.cos(2000 * np.pi * tk)

sd.play(xk, fs, blocking=True)
time.sleep(1)
sd.stop()
