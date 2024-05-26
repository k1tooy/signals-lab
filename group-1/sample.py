import numpy as np
import matplotlib.pyplot as plt

# Original Signal: x(t) = sin(2π10t)
def original_signal(t):
    return np.sin(2 * np.pi * 10 * t)

# Time interval for the continuous signal
t_continuous = np.linspace(0, 1, 1000)  # High-resolution time for continuous signal

# Sampling rate
fs = 10  # Hz
Ts = 1 / fs  # Sampling interval
n_samples = np.arange(0, 1, Ts)  # Discrete time points

# Continuous original signal
x_continuous = original_signal(t_continuous)

# Sampled signal at discrete time points
x_samples = original_signal(n_samples)

# Plot the original continuous-time signal
plt.figure(figsize=(10, 6))
plt.plot(t_continuous, x_continuous, label='Original Continuous Signal')
plt.stem(n_samples, x_samples, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Signal (10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Original Continuous Signal and Sampled Signal (10 Hz)')
plt.legend()
plt.grid(True)
plt.show()
