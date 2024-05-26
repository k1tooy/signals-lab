import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, butter, filtfilt
from scipy.io import wavfile
import sounddevice as sd

# Load the WAV file
fs, composite_signal = wavfile.read('amen-sample.wav')

# Normalize the signal if it's in integer format
if composite_signal.dtype == np.int16:
    composite_signal = composite_signal / 32768.0  # Normalize to range [-1, 1]

# If the signal is stereo, convert it to mono by averaging the channels
if len(composite_signal.shape) == 2:
    composite_signal = composite_signal.mean(axis=1)

# Define the correct time vector based on the length of the signal and the sampling rate
t = np.linspace(0, len(composite_signal) / fs, len(composite_signal), endpoint=False)

# FIR filter design
numtaps = 100  # Number of filter taps
cutoff = 100  # Cutoff frequency in Hz
fir_coeff = firwin(numtaps, cutoff, fs=fs)

# IIR filter design
iir_order = 1  # Order of the IIR filter
b, a = butter(iir_order, cutoff / (0.5 * fs), btype='low')

# Apply FIR filter
filtered_signal_fir = lfilter(fir_coeff, 1.0, composite_signal)

# Apply IIR filter
filtered_signal_iir = filtfilt(b, a, composite_signal)

plt.figure(figsize=(15, 10))

# Original Composite Signal
plt.subplot(3, 1, 1)
plt.plot(t, composite_signal)
plt.title("Original Composite Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# FIR Filtered Signal
plt.subplot(3, 1, 2)
plt.plot(t, filtered_signal_fir)
plt.title("FIR Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# IIR Filtered Signal
plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal_iir)
plt.title("IIR Filtered Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# Play the original and filtered signals
print("Now playing: original WAV")
sd.play(composite_signal, fs)
sd.wait()

print("Now playing: FIR filtered WAV")
sd.play(filtered_signal_fir, fs)
sd.wait()

print("Now playing: IIR filtered WAV")
sd.play(filtered_signal_iir, fs)
sd.wait()

# Write the filtered audio into WAV files
wavfile.write("fir_filtered.wav", fs, np.int16(filtered_signal_fir * 32767))
wavfile.write("iir_filtered.wav", fs, np.int16(filtered_signal_iir * 32767))

