import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft

f_s = 128
f1 = 21
f2 = 22

L1 = K1 = 128  # L = K
L2 = K2 = 64  # L = K

k1 = np.arange(0, K1)
k2 = np.arange(0, K2)

x_1k = np.cos(2 * np.pi * f1 / f_s * k1)
x_2k = np.cos(2 * np.pi * f2 / f_s * k2)

# a)
L3 = K3 = 20
fl3 = np.arange(0, L3) / L3 * f_s

x_3k = x_1k[:K3] + x_2k[:K3]

X_3fl = fft(x_3k, n=L3) / K3

# For zero-padding
L = 256
X_3fl_padded = fft(x_3k, n=L) / K3

fl = np.arange(0, L) / L * f_s

fig, axs = plt.subplots(2, 1)
fig.suptitle(
    "Plot represents the approximated magnitude spectrum of $X_{3}(f)$"
)

axs[0].stem(fl3, np.abs(X_3fl), "tab:blue", basefmt="tab:blue", label="Approx. $X_{3}(f)$, L=K")
axs[0].set_title("Magnitude Spectrum of $X_{3}(f)$, with 20 samples")
axs[0].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{3}(f)|$")
axs[0].set_xlim(0, 64)
axs[0].grid()
axs[0].legend()

# Task 3
axs[1].stem(fl, np.abs(X_3fl_padded), "tab:red", basefmt="tab:red", label="Approx. $X_{3}(f)$, zero padded, L > K")
axs[1].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{3}(f)|$")
axs[1].set_xlim(0, 64)
axs[1].grid()
axs[1].legend()



# b)
# 20 samples
fig, axs = plt.subplots(2, 1)
fig.suptitle(
    "Plot represents the approximated magnitude spectrum of $X_{3}(f)$, with zero padding but with different sampling rates"
)

axs[0].stem(fl, np.abs(X_3fl_padded), "tab:blue", basefmt="tab:blue", label="Approx. $X_{3}(f)$, zero padded, 20 samples")

# 64 samples
L3 = K3 = 64
fl3 = np.arange(0, L3) / L3 * f_s

x_3k = x_1k[:K3] + x_2k[:K3]

X_3fl_padded = fft(x_3k, n=L) / K3

fl = np.arange(0, L) / L * f_s


axs[0].stem(fl, np.abs(X_3fl_padded), "tab:red", basefmt="tab:red", label="Approx. $X_{3}(f)$, zero padded, 128 samples")
axs[0].set(xlabel=r"$f$ (Hz)", ylabel=r"$|X_{3}(f)|$")
axs[0].set_xlim(0, 64)
axs[0].grid()
axs[0].legend()

plt.show()
