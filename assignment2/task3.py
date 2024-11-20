import numpy as np
import matplotlib.pyplot as plt

# T0 = 5e-3
# alpha = 1000 * np.pi
# omega = 2 * np.pi * T0
#
# omega_interval = np.arange(-15e3, 15e3, dtype=float)
#
# c_n = np.zeros_like(omega_interval, dtype=complex)
#
# non_zero = omega_interval[omega_interval != 0]
# c_n[omega_interval != 0] = (-1) ** (non_zero) * 1j / (non_zero * np.pi)
#
#
# H_w = np.zeros_like(omega_interval, dtype=complex)
# H_w = alpha**2 / (-(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2)

T0 = 5e-3
omega_0 = 2 * np.pi / T0
alpha = 1000 * np.pi

n = np.arange(-12, 12, dtype=float)
omega_interval = n * omega_0

c_n = np.zeros_like(n, dtype=complex)

non_zero = n[n != 0]
c_n[n != 0] = (-1) ** non_zero * 1j / (non_zero * np.pi)

X_w = 2 * np.pi * c_n


omega_interval_H_w = np.arange(-15e3, 15e3, dtype=float)
H_w = np.zeros_like(n, dtype=complex)

H_w = alpha**2 / (
    -(omega_interval_H_w**2) + 2 * alpha * 1j * omega_interval_H_w + alpha**2
)


# Y_w = X_w * H_w
# Y_w = []
# for w in range(len(X_w)):
#
#    Y_w.append(X_w[w] * (alpha**2 / (-(w**2) + 2 * alpha * 1j * w + alpha**2)))
#
H_w_ach = alpha**2 / (-(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2)
Y_w = X_w * H_w_ach


magnitude_X = np.abs(X_w)
phase_X = []
for w in range(len(n)):
    angle = np.angle(X_w[w])

    if w < len(n) / 2 and angle < 0:
        phase_X.append(angle + 2 * np.pi)
    elif w > len(n) / 2 and angle > 0:
        phase_X.append(angle - 2 * np.pi)
    else:
        phase_X.append(angle)



magnitude_H = np.abs(H_w)
phase_H = np.angle(H_w)

magnitude_Y = np.abs(Y_w)
# phase_Y = np.angle(Y_w)

phase_Y = []
for w in range(len(n)):
    angle = np.angle(Y_w[w])

    if w < len(n) / 2 and angle < 0:
        phase_Y.append(angle + 2 * np.pi)
    elif w > len(n) / 2 and angle > 0:
        phase_Y.append(angle - 2 * np.pi)
    else:
        phase_Y.append(angle)




fig, axs = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Magnitude and Phase Spectra: Input $X(\omega)$ vs. Output $Y(\omega)$")

# Magnitude
axs[0].stem(
    omega_interval,
    magnitude_X,
    linefmt="b",
    markerfmt="bo",
    basefmt=" ",
    label="$|X(\omega)|$",
)
axs[0].plot(
    omega_interval_H_w,
    magnitude_H,
    "tab:orange",
    label="$|H(\omega)|$",
)
axs[0].stem(
    omega_interval,
    magnitude_Y,
    linefmt="r-",
    markerfmt="ro",
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
axs[1].plot(
    omega_interval_H_w,
    phase_H,
    "tab:orange",
    label="$\\angle H(\omega)$",
)
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
