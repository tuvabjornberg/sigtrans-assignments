import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import time

# Task 1 

# x1
T1 = 0.01 

#x2
f2 = 1000

interval = [0, 5]
A = 1

dt = 0.00001

t = np.arange(interval[0], interval[1], dt)

x1 = A * np.sin((1 / T1) * 2 * np.pi * t) # f = 1/T, w= 2pif
x2 = A * np.sin(f2 * 2 * np.pi * t)

fig, ax = plt.subplots()

ax.title.set_text("Plot of the sinusoid signals x1 and x2")
ax.plot(t, x1, label='x1')
ax.plot(t, x2, label='x2')
ax.set_xlabel('t (s)')
ax.set_ylabel('Amplitude')
ax.legend()
ax.set_xlim([0, 0.01])
ax.set_ylim([-1, 1])
plt.show()

sd.play(x2, 1/dt, blocking=True)
time.sleep(1)
sd.stop()
