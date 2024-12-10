import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sounddevice as sd
import time

# Filter
z, p, k = signal.butter(5, 6800 * np.pi, analog=True, output="zpk")
H = signal.ZerosPolesGain(z, p, k)
w, magnitude, phase = signal.bode(H, n=1000)

magnitude = 10 ** (magnitude / 20)
freq = w / (np.pi * 2)

# Plot the magnitude response of the filter
plt.figure()
plt.plot(freq, magnitude)
plt.xscale("log")
plt.title("Magnitude of a 5th order Butterworth filter")
plt.xlabel("Frequency (Hz)")
plt.xlim([1000, 10000])
plt.ylabel("Magnitude")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.show()

# Signal
t = [0, 3]
fs = 40e3
fs_resampled = 8e3
Ts = 1 / fs
K = t[1] * fs


x = sd.rec(int(K), fs, channels=1, blocking=True)
sd.play(x, fs, blocking=True)  # Original recording, 40kHz
print("Original, 40kHz done")


xs = x[::5]  # pick every 5th sample in the recording, --> 8kHz
sd.play(xs, fs_resampled, blocking=True)
print("Resampled, 8kHz done")


tk = np.arange(t[0], t[1], Ts)
tf, xf, __ = signal.lsim(H, x, tk)

xf = xf[::5]  # pick every 5th sample in the recording, --> 8kHz
sd.play(xf, fs_resampled, blocking=True)
print("Resampled + filter, 8kHz done")
