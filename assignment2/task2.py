import numpy as np
import matplotlib.pyplot as plt

T0 = 5e-3
alpha = 1000 * np.pi
omega_0 = 2 * np.pi / T0

#n = np.arange(-12, 12, dtype=float)
#omega_interval = n * omega_0
omega_interval = np.arange(-15e3, 15e3, dtype=float)


H_w = np.zeros_like(omega_interval, dtype=complex)

#non_zero = omega_interval[omega_interval != 0]
H_w = alpha**2 / (-(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2)

magnitude = np.abs(H_w)
phase = np.angle(H_w) 

fig, axs = plt.subplots(1, 2)
fig.suptitle(
    "Plot represents the magnitude and phase shift of the frequency response H(w)"
)

#axs[0].stem(omega_interval, magnitude, basefmt=" ")
axs[0].plot(omega_interval, magnitude)
axs[0].set_title("Magnitude Spectrum of $X(\omega)$")
axs[0].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$|X(\omega)|$")
axs[0].grid()

#axs[1].stem(omega_interval, phase, basefmt=" ")
axs[1].plot(omega_interval, phase)
axs[1].set_title("Phase Spectrum of $X(\omega)$")
axs[1].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$\angle X(\omega)$ (rad)")
axs[1].grid()

# fig.legend()
plt.show()
