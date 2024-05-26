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

# Only keep the positive frequencies
positive_frequencies = frequencies[:N // 2]
positive_X_magnitude = 2 * X_magnitude[:N // 2]  # Multiply by 2 to account for the symmetrical nature of FFT

# Plot the magnitude of the Fourier transform
plt.figure(figsize=(12, 6))
plt.plot(positive_frequencies, positive_X_magnitude, label='Magnitude of Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Magnitude of the Fourier Transform of the Signal')
plt.grid(True)
plt.legend()
plt.show()

