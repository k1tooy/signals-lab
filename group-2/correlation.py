import numpy as np
import matplotlib.pyplot as plt

# Define two signals for cross-correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

# Define a signal for auto-correlation
z = np.array([1, 2, 3, 4, 3, 2, 1])

# Auto-correlation in time domain
def auto_correlation(signal):
    result = np.correlate(signal, signal, mode='full')
    return result[result.size // 2:]

# Cross-correlation in time domain
def cross_correlation(signal1, signal2):
    result = np.correlate(signal1, signal2, mode='full')
    return result

# Auto-correlation using FFT
def auto_correlation_fft(signal):
    signal_fft = np.fft.fft(signal, n=2*len(signal)-1)
    result = np.fft.ifft(signal_fft * np.conj(signal_fft)).real
    return result[result.size // 2:]

# Cross-correlation using FFT
def cross_correlation_fft(signal1, signal2):
    n = len(signal1) + len(signal2) - 1
    signal1_fft = np.fft.fft(signal1, n)
    signal2_fft = np.fft.fft(signal2, n)
    result = np.fft.ifft(signal1_fft * np.conj(signal2_fft)).real
    return result

# Calculate correlations
auto_corr_time = auto_correlation(z)
cross_corr_time = cross_correlation(x, y)
auto_corr_freq = auto_correlation_fft(z)
cross_corr_freq = cross_correlation_fft(x, y)

# Plot the results
plt.figure(figsize=(15, 10))

# Plot auto-correlation in time domain
plt.subplot(2, 2, 1)
plt.stem(auto_corr_time)
plt.title('Auto-correlation (Time Domain)')
plt.xlabel('Lag')
plt.ylabel('Amplitude')

# Plot cross-correlation in time domain
plt.subplot(2, 2, 2)
plt.stem(cross_corr_time)
plt.title('Cross-correlation (Time Domain)')
plt.xlabel('Lag')
plt.ylabel('Amplitude')

# Plot auto-correlation using FFT
plt.subplot(2, 2, 3)
plt.stem(auto_corr_freq)
plt.title('Auto-correlation (Frequency Domain)')
plt.xlabel('Lag')
plt.ylabel('Amplitude')

# Plot cross-correlation using FFT
plt.subplot(2, 2, 4)
plt.stem(cross_corr_freq)
plt.title('Cross-correlation (Frequency Domain)')
plt.xlabel('Lag')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

