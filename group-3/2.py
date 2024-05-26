import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# Define the parameters
f1 = 1   # Hz
f2 = 50  # Hz
f3 = 300 # Hz
cut_off_frequency = 250  # Hz
sampling_rate = 1000  # Hz
sampling_interval = 1 / sampling_rate
t = np.arange(0, 1, sampling_interval)  # 1 second of data

# Define the original signal
def original_signal(t, f1, f2, f3):
    return np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t) + 0.2 * np.sin(2 * np.pi * f3 * t)

# Generate the original signal
x = original_signal(t, f1, f2, f3)

# Design low-pass and high-pass filters
def butter_lowpass(cut_off, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cut_off / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_highpass(cut_off, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cut_off / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

# Apply filters to the signal
def filter_signal(data, b, a):
    return lfilter(b, a, data)

# Low-pass filter
b_low, a_low = butter_lowpass(cut_off_frequency, sampling_rate)
x_low = filter_signal(x, b_low, a_low)

# High-pass filter
b_high, a_high = butter_highpass(cut_off_frequency, sampling_rate)
x_high = filter_signal(x, b_high, a_high)

# Compute frequency responses
w_low, h_low = freqz(b_low, a_low, worN=8000)
w_high, h_high = freqz(b_high, a_high, worN=8000)

# Plotting
fig, axes = plt.subplots(5, 1, figsize=(15, 25))

# (a) Original signal
axes[0].plot(t, x)
axes[0].set_title('Original Signal')
axes[0].set_xlabel('Time [s]')
axes[0].set_ylabel('Amplitude')
axes[0].grid()

# (b) Low-pass filtered signal
axes[1].plot(t, x_low)
axes[1].set_title('Low-pass Filtered Signal')
axes[1].set_xlabel('Time [s]')
axes[1].set_ylabel('Amplitude')
axes[1].grid()

# (c) High-pass filtered signal
axes[2].plot(t, x_high)
axes[2].set_title('High-pass Filtered Signal')
axes[2].set_xlabel('Time [s]')
axes[2].set_ylabel('Amplitude')
axes[2].grid()

# (d) Low-pass filter frequency response
axes[3].plot(0.5 * sampling_rate * w_low / np.pi, np.abs(h_low))
axes[3].set_title('Low-pass Filter Frequency Response')
axes[3].set_xlabel('Frequency [Hz]')
axes[3].set_ylabel('Gain')
axes[3].grid()

# (e) High-pass filter frequency response
axes[4].plot(0.5 * sampling_rate * w_high / np.pi, np.abs(h_high))
axes[4].set_title('High-pass Filter Frequency Response')
axes[4].set_xlabel('Frequency [Hz]')
axes[4].set_ylabel('Gain')
axes[4].grid()

plt.tight_layout(pad=10.0)
plt.show()

