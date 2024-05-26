import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time signal
def x(t):
    return np.sin(2 * np.pi * 5 * t)

# Time interval
t_continuous = np.linspace(0, 1, 1000)  # High-resolution time for continuous signal

# Sampling rate
fs = 20  # Hz
Ts = 1 / fs  # Sampling interval
n_samples = np.arange(0, 1, Ts)  # Discrete time points

# Sample the signal at discrete time points
x_samples = x(n_samples)

# Plot the continuous signal and the sampled signal
plt.figure(figsize=(10, 6))
plt.plot(t_continuous, x(t_continuous), label='Continuous-Time Signal')
plt.stem(n_samples, x_samples, linefmt='-', markerfmt='ro', basefmt='r-', label='Discrete Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Continuous-Time Signal and Sampled Signal')
plt.legend(loc='lower left', frameon=False)
plt.grid(True)
plt.show()

