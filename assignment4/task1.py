import numpy as np
import matplotlib.pyplot as plt


f1 = 21
f2 = 22

# x_1t = np.cos(21 * t)
X_1w = [np.pi * -f1, np.pi * f1]

# x_2t = np.cos(22 * t)
X_2w = [np.pi * -f2, np.pi * f2]


fig, axs = plt.subplots(1, 2)
fig.suptitle("Plot represents the magnitude of $X_{1}(f) and X_{2}(f)$")

axs[0].stem([-f1, f1], [0.5, 0.5], basefmt=" ", markerfmt="^")
axs[0].set_title("Magnitude Spectrum of $X_{1}(f)$")
axs[0].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{1}(f)|$")
axs[0].set_xlim(0, 64)
axs[0].grid()


axs[1].stem([-f2, f2], [0.5, 0.5], basefmt=" ", markerfmt="^")
axs[1].set_title("Magnitude Spectrum of $X_{2}(f)$")
axs[1].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{2}(f)|$")
axs[1].set_xlim(0, 64)
axs[1].grid()


plt.show()
