import numpy as np
import matplotlib.pyplot as plt


T0 = 5e-3
omega_0 = 2 * np.pi / T0

n = np.arange(-12, 12, dtype=float)
omega_interval = n * omega_0

c_n = np.zeros_like(n, dtype=complex)

non_zero = n[n != 0]
c_n[n != 0] = (-1) ** non_zero * 1j / (non_zero * np.pi)

X_w = 2 * np.pi * c_n

magnitude = np.abs(X_w)

phase = []
for w in range(len(n)):
    angle = np.angle(X_w[w])

    if w < len(n) / 2 and angle < 0:
        phase.append(angle + 2 * np.pi)
    elif w > len(n) / 2 and angle > 0:
        phase.append(angle - 2 * np.pi)
    else:
        phase.append(angle)


# phase = np.angle(X_w)

fig, axs = plt.subplots(1, 2)
fig.suptitle(
    "Plot represents the magnitude and phase shift of the frequency response H(s)"
)

axs[0].stem(omega_interval, magnitude, basefmt=" ")
axs[0].set_title("Magnitude Spectrum of $X(s)$")
axs[0].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$|X(\omega)|$")
axs[0].grid()

axs[1].stem(omega_interval, phase, basefmt=" ")
axs[1].set_title("Phase Spectrum of $X(s)$")
axs[1].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$\angle X(\omega)$ (rad)")
axs[1].grid()

# fig.legend()
plt.show()
