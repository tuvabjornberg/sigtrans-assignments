import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft

f_s = 128
f1 = 21
f2 = 22

# a)
L1 = K1 = 128  # L = K
L2 = K2 = 64  # L = K

k1 = np.arange(0, K1)
k2 = np.arange(0, K2)

x_1k = np.cos(2 * np.pi * f1 / f_s * k1)
x_2k = np.cos(2 * np.pi * f2 / f_s * k2)

X_1l = fft(x_1k)
X_2l = fft(x_2k)

fl1 = np.arange(0, L1) / L1 * f_s
fl2 = np.arange(0, L2) / L2 * f_s


X_1fl = 1 / K1 * X_1l
X_2fl = 1 / K2 * X_2l

# b)
L = 256

X_1l_padded = fft(x_1k, n=L) / K1
X_2l_padded = fft(x_2k, n=L) / K2

fl = np.arange(0, L) / L * f_s


fig, axs = plt.subplots(1, 2)
fig.suptitle(
    "Plot represents the approximated and expected magnitude spectrum of $X_{1}(f)$ and $X_{2}(f)$"
)

# Task 2 b)
axs[0].stem(
    fl, np.abs(X_1l_padded), "g", basefmt="g", label="Approx. $X_{1}(f)$ zero padded, L>K"
)
# Task 2 a)
axs[0].stem(fl1, np.abs(X_1fl), "tab:orange", basefmt="orange", label="Approx. $X_{1}(f)$, L=K")
# Task 1
axs[0].stem(
    [-f1, f1], [0.5, 0.5], basefmt=" ", linefmt=":", label="Expected $X_{1}(f)$"
)

axs[0].set_title("Magnitude Spectrum of $X_{1}(f)$")
axs[0].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{1}(f)|$")
axs[0].set_xlim(0, 64)
axs[0].grid()
axs[0].legend()


# Task 2 b)
axs[1].stem(
    fl, np.abs(X_2l_padded), "g", basefmt='g', label="Approx. $X_{2}(f)$ zero padded, L>K"
)
# Task 2 a)
axs[1].stem(fl2, np.abs(X_2fl), "tab:orange", basefmt="orange", label="Approx. $X_{2}(f)$, L=K")
# Task 1
axs[1].stem(
    [-f2, f2], [0.5, 0.5], basefmt=" ", linefmt=":", label="Expected $X_{2}(f)$"
)

axs[1].set_title("Magnitude Spectrum of $X_{2}(f)$")
axs[1].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{2}(f)|$")
axs[1].set_xlim(0, 64)
axs[1].grid()
axs[1].legend()


plt.show()
