import numpy as np
import scipy
import matplotlib.pyplot as plt
import sounddevice as sd
import time

t = [0, 5]

fs = 40e3
Ts = 1 / fs
K = t[1] * fs

x = sd.rec(int(K), fs, channels=1, blocking=True)

print("Original")
sd.play(x, fs, blocking=True)  # Original call, 40kHz sampling rate

print(x.shape)
x = x[::5]  # pick every 5th sample in the recording, --> 8kHz
print(x.shape)

print("Resampled")
sd.play(x, 8e3, blocking=True)  # Resampled call, 8kHz sampling rate
