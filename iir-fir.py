import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin

# Original Signal: x(t) = sin(2π3t) + sin(2π7t)
def original_signal(t):
    return np.sin(2 * np.pi * 3 * t) + np.sin(2 * np.pi * 7 * t)

# Time interval
t = np.linspace(0, 1, 1000)  # High-resolution time for continuous signal

# Original Signal
x_original = original_signal(t)

# Design an IIR Butterworth filter with a cutoff frequency of 5 Hz
def butterworth_filter(data, cutoff_frequency, sampling_rate, order=4):
    nyquist_frequency = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist_frequency
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data

# Design an FIR filter with a cutoff frequency of 5 Hz using 21 taps
def fir_filter(data, cutoff_frequency, sampling_rate, num_taps=21):
    nyquist_frequency = 0.5 * sampling_rate
    cutoff = cutoff_frequency / nyquist_frequency
    taps = firwin(num_taps, cutoff, window='hamming')
    filtered_data = np.convolve(data, taps, mode='same')
    return filtered_data

# Apply the IIR Butterworth filter
cutoff_frequency = 5  # Hz
sampling_rate = 1000  # Hz
filtered_iir = butterworth_filter(x_original, cutoff_frequency, sampling_rate)

# Apply the FIR filter
filtered_fir = fir_filter(x_original, cutoff_frequency, sampling_rate)

fig, ax = plt.subplots(2, 1, figsize=(10, 8), facecolor='none')

# Plot Original Signal
ax[0].plot(t, x_original, label='Original Signal')
ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Original Signal')
ax[0].legend()
ax[0].grid(True)

# Plot Filtered Outputs
ax[1].plot(t, filtered_iir, label='IIR Butterworth Filter Output')
ax[1].plot(t, filtered_fir, label='FIR Filter Output')
ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Filtered Outputs of IIR and FIR Filters')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()
