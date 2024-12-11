import numpy as np
import matplotlib.pyplot as plt


f1 = 21
f2 = 22

f_s = 128  # Sampling frequency
K = 20  # Number of samples
k = np.arange(0, K)


x_1k = np.cos(2 * np.pi * f1 / f_s * k)
x_2k = np.cos(2 * np.pi * f2 / f_s * k)


fig, axs = plt.subplots(1, 2)
fig.suptitle("Plot of sampled cosine signals")

axs[0].stem(k, x_1k, "tab:orange")
axs[0].set_title(r"The signal $x_{1}[k]$")
axs[0].set(xlabel=r"k", ylabel=r"$x_{1}[k]$")
axs[0].set_xlim(0, 20)
axs[0].grid()
axs[0].set_xticks(k)

axs[1].stem(k, x_2k, "tab:orange")
axs[1].set_title("The signal $x_{2}[k]$")
axs[1].set(xlabel=r"k", ylabel=r"$x_{2}[k]$")
axs[1].set_xlim(0, 20)
axs[1].grid()
axs[1].set_xticks(k)

plt.show()
