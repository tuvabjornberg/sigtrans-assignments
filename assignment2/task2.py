import numpy as np
import matplotlib.pyplot as plt


T0 = 5e-3
alpha = 1000 * np.pi

omega_interval = np.arange(-15e3, 15e3, dtype=float)

# Continious signal
H_w = np.zeros_like(omega_interval, dtype=complex)
H_w = alpha**2 / (-(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2)

magnitude = np.abs(H_w)
phase = np.angle(H_w)

fig, axs = plt.subplots(1, 2)
fig.suptitle(
    "Plot represents the magnitude and phase shift of the frequency response H($\omega$)"
)

axs[0].plot(omega_interval, magnitude, "tab:orange")
axs[0].set_title("Magnitude Spectrum of $H(\omega)$")
axs[0].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$|H(\omega)|$")
axs[0].grid()

axs[1].plot(omega_interval, phase, "tab:orange")
axs[1].set_title("Phase Spectrum of $H(\omega)$")
axs[1].set(xlabel=r"$\omega$ (rad/s)", ylabel=r"$\angle H(\omega)$ (rad)")
axs[1].grid()

plt.show()
