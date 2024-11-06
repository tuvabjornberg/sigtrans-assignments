import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

alpha = 1000 * np.pi
dt = 0.00001

t = np.arange(0, 0.02, dt)

h = alpha**2 * t * np.exp(-alpha * t) * (t >= 0)  # u(1) = 1 when t >= 0

d = np.zeros(t.shape)
d[0] = 1 / dt

y = dt * signal.convolve(d, h, method="direct")
y = y[0 : d.shape[0]]


plt.title("Impulse response and its convolution with the unit response function")
plt.plot(t, h, label="h(t)")
plt.plot(t, y, label="h(t) * δ(t)", linestyle="--")
plt.xlabel("time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.xlim([0, 0.003])
plt.show()
