import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import time

# Task 1

# x1
T1 = 0.01

# x2
f2 = 1000

interval = [0, 5]
A = 1

dt = 0.00001

t = np.arange(interval[0], interval[1], dt)

x1 = A * np.sin((1 / T1) * 2 * np.pi * t)  # f = 1/T, w= 2pif
x2 = A * np.sin(f2 * 2 * np.pi * t)

fig, (ax, ax2) = plt.subplots(1, 2)

fig.suptitle("Plot of the sinusoid signals x1 and x2")
ax.plot(t, x1, label="x1, sin(200π*t)")
ax.set_xlabel("t (s)")
ax.set_ylabel("Amplitude")
ax.set_xlim([0, 0.01])
ax.set_ylim([-1, 1])

ax2.plot(t, x2, "tab:orange", label="x2, sin(2000π*t)")
ax2.set_xlabel("t (s)")
ax2.set_ylabel("Amplitude")
ax2.set_xlim([0, 0.01])
ax2.set_ylim([-1, 1])

fig.legend()
plt.show()

sd.play(x2, 1 / dt, blocking=True)
time.sleep(1)
sd.stop()
