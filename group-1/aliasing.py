import numpy as np
import matplotlib.pyplot as plt

# Original Signal: x(t) = sin(2π25t)
def original_signal(t):
    return np.sin(2 * np.pi * 25 * t)

# Time interval
t_continuous = np.linspace(0, 1, 1000)  # High-resolution time for continuous signal

# Sampling rate
fs = 10  # Hz
Ts = 1 / fs  # Sampling interval
n_samples = np.arange(0, 1, Ts)  # Discrete time points

# Sample the signal at discrete time points
x_samples = original_signal(n_samples)

# Plot the original signal and the sampled signal
plt.figure(figsize=(10, 6))
plt.plot(t_continuous, original_signal(t_continuous), label='Original Signal')
plt.stem(n_samples, x_samples, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Original Signal and Sampled Signal (Aliasing)')
plt.legend(loc="lower left")
plt.grid(True)
plt.show()
