import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

# x1
T1 = 0.01

# x2
f2 = 1000

A = 1

dt = 0.00001
t = np.arange(0, 0.02, dt)

x1 = A * np.sin((1 / T1) * 2 * np.pi * t)  # f = 1/T, w= 2pif
x2 = A * np.sin(f2 * 2 * np.pi * t)
x3 = x1 + x2

# Apply the signal x3(t) = x1(t) + x2(t) to the system to obtain y3(t). Plot y3(t) for
# the interval 0 s ≤ t ≤ 20 ms together with y1(t) + y2(t) from the Task 3 in a new
# figure. Compare the results and explain it.

alpha = 1000 * np.pi

h = alpha**2 * t * np.exp(-alpha * t) * (t >= 0)  # u(1) = 1 when t >= 0

d = np.zeros(t.shape)
d[0] = 1 / dt

y1 = dt * signal.convolve(x1, h, method="direct")
y1 = y1[0 : x1.shape[0]]

y2 = dt * signal.convolve(x2, h, method="direct")
y2 = y2[0 : x2.shape[0]]

y3 = dt * signal.convolve(x3, h, method="direct")
y3 = y3[0 : x3.shape[0]]

ycombo = y1 + y2

fig, axs = plt.subplots(1, 2)
fig.suptitle("Plot represents convolution of sum, and sum of convolutions, of sinusoidal signals ")

axs[0].plot(t, y3, label="y3")
axs[0].set_title('Convolution of sum, y3')
axs[0].set_xlim([0, 0.02])
axs[0].set_ylim([-1.2, 1.2])

axs[1].plot(t, ycombo, 'tab:orange', label="y1 + y2")
axs[1].set_title('Sum of convolutions, y1 + y2')
axs[1].set_xlim([0, 0.02])
axs[1].set_ylim([-1.2, 1.2])


for ax in axs.flat:
    ax.set(xlabel='time (s)', ylabel='Amplitude')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

fig.legend()
plt.show()
