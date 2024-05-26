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

# Compute the Fourier transform
X = np.fft.fft(x)
N = len(X)
X_magnitude = np.abs(X) / N  # Magnitude of the Fourier transform

# Create the frequency vector
frequencies = np.fft.fftfreq(N, d=sampling_interval)

# Shift the zero frequency component to the center
X_magnitude_shifted = np.fft.fftshift(X_magnitude)
frequencies_shifted = np.fft.fftshift(frequencies)

# Plot the magnitude of the shifted Fourier transform
plt.figure(figsize=(12, 6))
plt.plot(frequencies_shifted, X_magnitude_shifted, label='Magnitude of Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Magnitude of the Fourier Transform of the Signal (Shifted)')
plt.grid(True)
plt.legend()
plt.show()
