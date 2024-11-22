import numpy as np
import matplotlib.pyplot as plt


T0 = 5e-3
omega_0 = 2 * np.pi / T0
alpha = 1000 * np.pi

n = np.arange(-12, 12, dtype=float)
omega_interval = n * omega_0

# X(w)
c_n = np.zeros_like(n, dtype=complex)
non_zero = n[n != 0]
c_n[n != 0] = (-1) ** non_zero * 1j / (non_zero * np.pi)

X_w = 2 * np.pi * c_n

magnitude_X = np.abs(X_w)
phase_X = []
# Phase unwrapping
for w in range(len(n)):
    angle = np.angle(X_w[w])

    if w < len(n) / 2 and angle < 0:
        phase_X.append(angle + 2 * np.pi)
    elif w > len(n) / 2 and angle > 0:
        phase_X.append(angle - 2 * np.pi)
    else:
        phase_X.append(angle)

# H(w)
omega_interval_H_w = np.arange(-15e3, 15e3, dtype=float)

H_w_value = alpha**2 / (
    -(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2
)

magnitude_H = np.abs(H_w_value)
phase_H = np.angle(H_w_value)

# Y(w)
# Simplified, we don't have to make Y(w) and take mag/phase
magnitude_Y = magnitude_X * magnitude_H
phase_Y = phase_X + phase_H

# Only for plot of H(w)
# H_w = alpha**2 / (
# H_w = np.zeros_like(n, dtype=complex)
#    -(omega_interval_H_w**2) + 2 * alpha * 1j * omega_interval_H_w + alpha**2
# )

# magnitude_H_cont = np.abs(H_w)
# phase_H_cont = np.angle(H_w)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Magnitude and Phase Spectra: Input $X(\omega)$ vs. Output $Y(\omega)$")

# Magnitude
axs[0].stem(
    omega_interval,
    magnitude_X,
    linefmt="b",
    markerfmt="b^",
    basefmt=" ",
    label="$|X(\omega)|$",
)
# With H(w)
# axs[0].plot(
#    omega_interval_H_w,
#    magnitude_H_cont,
#    "tab:orange",
#    label="$|H(\omega)|$",
# )
axs[0].stem(
    omega_interval,
    magnitude_Y,
    linefmt="r-",
    markerfmt="r^",
    basefmt=" ",
    label="$|Y(\omega)|$",
)
axs[0].set_title("Magnitude Spectrum")
axs[0].set(xlabel=r"$\omega$ (rad/s)", ylabel="Magnitude")
axs[0].grid()
axs[0].legend()

# Phase
axs[1].stem(
    omega_interval,
    phase_X,
    linefmt="b",
    markerfmt="bo",
    basefmt=" ",
    label="$\\angle X(\omega)$",
)
# With H(w)
# axs[1].plot(
#    omega_interval_H_w,
#    phase_H_cont,
#    "tab:orange",
#    label="$\\angle H(\omega)$",
# )
axs[1].stem(
    omega_interval,
    phase_Y,
    linefmt="r-",
    markerfmt="ro",
    basefmt=" ",
    label="$\\angle Y(\omega)$",
)
axs[1].set_title("Phase Spectrum")
axs[1].set(xlabel=r"$\omega$ (rad/s)", ylabel="Phase (rad)")
axs[1].grid()
axs[1].legend()

plt.show()
