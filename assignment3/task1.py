import numpy as np
import scipy
import matplotlib.pyplot as plt
import sounddevice as sd
import time


t = [0, 5]
# a
Ts = 0.1e-3
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


# Comp. against other Ts
# Ts2 = 0.1e-3
# fs2 = 1 / Ts
# tk2 = np.arange(t[0], t[1], Ts)
# xk2 = np.cos(2000 * np.pi * tk)
# sd.play(xk2, fs2, blocking=True)
# time.sleep(1)

# Plot
# fig, axs = plt.subplots(1, 2)
# fig.suptitle("Plot represents the magnitude and phase shift of X($\omega$)")
#
# axs[0].stem(tk, xk, basefmt=" ", markerfmt="^")
# axs[0].set_title("1st freq")
# axs[0].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$|X(\omega)|$")
# axs[0].grid()
#
# axs[1].stem(tk2, xk2, basefmt=" ")
# axs[1].set_title("2nd freq")
# axs[1].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$\angle X(\omega)$ (rad)")
# axs[1].grid()
#
# plt.show()
