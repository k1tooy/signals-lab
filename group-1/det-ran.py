import numpy as np
import matplotlib.pyplot as plt

# Define the deterministic signal
def deterministic_signal(t):
    return np.cos(2 * np.pi * 3 * t)

# Time interval
t = np.linspace(0, 1, 1000)  # High-resolution time for both signals

# Generate the deterministic signal
x_deterministic = deterministic_signal(t)

# Generate the random (Gaussian noise) signal
mean = 0
std_dev = 1
x_random = np.random.normal(mean, std_dev, len(t))

# Plot both signals
fig, ax = plt.subplots(2, 1, figsize=(10, 8), facecolor='none')

# Plot deterministic signal
ax[0].plot(t, x_deterministic, label='Deterministic Signal: $x(t) = \cos(2\pi 3t)$')
ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Deterministic Signal')
ax[0].legend(loc='upper right', frameon=False)
ax[0].grid(True)
ax[0].set_facecolor('none')

# Plot random signal
ax[1].plot(t, x_random, label='Random Signal: Gaussian Noise')
ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Random Signal')
ax[1].legend(loc='upper right', frameon=False)
ax[1].grid(True)
ax[1].set_facecolor('none')

# Set figure background to be transparent
fig.patch.set_alpha(0.0)

plt.tight_layout()
plt.show()

