import numpy as np
import matplotlib.pyplot as plt


T0 = 5e-3
omega_0 = 2 * np.pi / T0
alpha = 1000 * np.pi

n = np.arange(-21, 21, dtype=float)
omega_interval = n * omega_0

# X(w)
c_n = np.zeros_like(n, dtype=complex)
non_zero = n[n != 0]
c_n[n != 0] = (-1) ** non_zero * 1j / (non_zero * np.pi)

X_w = 2 * np.pi * c_n

# H(w)
H_w_value = alpha**2 / (
    -(omega_interval**2) + 2 * alpha * 1j * omega_interval + alpha**2
)

# Y(w)
Y_w = X_w * H_w_value


# The output function y(t)
def y_t(t, N):
    y_t = 0

    for n in range(-N, N + 1):
        y_t += Y_w[len(Y_w) // 2 + n] * np.exp(1j * n * omega_0 * t) / (2 * np.pi)

    return np.real(y_t)


# Time vector to plot over
t = np.linspace(0, 15e-3, 1000)

fig, axs = plt.subplots(1, 1, figsize=(12, 6))

axs.plot(t, y_t(t, 1), "tab:orange", label="N=1")
axs.plot(t, y_t(t, 2), "tab:blue", label="N=2")
axs.plot(t, y_t(t, 10), "tab:green", label="N=10")
axs.plot(t, y_t(t, 20), "tab:pink", label="N=20")

axs.set_title("Output function y(t), with different N components")
axs.set(xlabel=r"t (s)", ylabel="y(t)")
axs.grid()
axs.legend()

plt.show()
