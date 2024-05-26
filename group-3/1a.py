import numpy as np
import matplotlib.pyplot as plt

# Define the signal
def signal(t):
    return np.sin(2 * np.pi * 15 * t) + np.sin(2 * np.pi * 20 * t)

# Define the time vector
sampling_interval = 1 / 50  # 50 samples per second
t = np.arange(0, 10, sampling_interval)  # Time vector from 0 to 10 seconds in increments of 1/50 seconds

# Generate the signal
x = signal(t)

# Plot the signal
plt.figure(figsize=(12, 6))
plt.plot(t, x, label='$x(t) = \sin(2\pi \cdot 15t) + \sin(2\pi \cdot 20t)$')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Signal with Frequency Components of 15 Hz and 20 Hz')
plt.legend()
plt.grid(True)
plt.show()

