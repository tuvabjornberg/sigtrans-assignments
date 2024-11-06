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


# Apply the signals x1(t) and x2(t) to the system in Task 2 to obtain the outputs y1(t)
# and y2(t). Plot the outputs together in a new figure for the interval 0 s ≤ t ≤ 20 ms
# and discuss how the system affects the two inputs. Are both signals affected in the
# same way? What is affected and how much? What does the result indicate about
# the system?

alpha = 1000 * np.pi

h = alpha**2 * t * np.exp(-alpha * t) * (t >= 0)  # u(1) = 1 when t >= 0

d = np.zeros(t.shape)
d[0] = 1 / dt

y1 = dt * signal.convolve(x1, h, method="direct")
y1 = y1[0 : x1.shape[0]]

y2 = dt * signal.convolve(x2, h, method="direct")
y2 = y2[0 : x2.shape[0]]



fig, axs = plt.subplots(2, 2)
fig.suptitle("Plot of the sinusoid signals x1 and x2 before and after convolution")

axs[0, 0].plot(t, x1, label="x1")
axs[0, 0].set_title('x1')
axs[0, 0].set_xlim([0, 0.02])
axs[0, 0].set_ylim([-1, 1])

axs[0, 1].plot(t, y1, 'tab:orange', label="x1 convoluted")
axs[0, 1].set_title('x1 convoluted')
axs[0, 1].set_xlim([0, 0.02])
axs[0, 1].set_ylim([-1, 1])

axs[1, 0].plot(t, x2, 'tab:green', label="x2")
axs[1, 0].set_title('x2')
axs[1, 0].set_xlim([0, 0.02])
axs[1, 0].set_ylim([-1, 1])

axs[1, 1].plot(t, y2, 'tab:red', label="x2 concoluted")
axs[1, 1].set_title('x2 convoluted')
axs[1, 1].set_xlim([0, 0.02])
axs[1, 1].set_ylim([-1, 1])

for ax in axs.flat:
    ax.set(xlabel='time (s)', ylabel='Amplitude')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

fig.legend()
plt.show()
