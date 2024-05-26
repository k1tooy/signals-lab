import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk

# Define the filter design
def design_filter(filter_type):
    if filter_type == 'lowpass':
        b = [0.2, 0.2, 0.2, 0.2, 0.2]  # Moving average filter (FIR)
        a = [1]                        # All-pole filter
    elif filter_type == 'highpass':
        b = [1, -1]                   # Difference filter (FIR)
        a = [1, -0.9]                 # Single-pole filter
    elif filter_type == 'bandpass':
        b = [0.2, 0, -0.2]            # FIR band-pass filter
        a = [1, -1.6, 0.64]           # IIR band-pass filter
    elif filter_type == 'bandstop':
        b = [1, -1.6, 1]              # FIR band-stop filter
        a = [1, -1.6, 0.64]           # IIR band-stop filter
    else:
        raise ValueError('Unknown filter type')
    return b, a

# Plot the frequency response
def plot_frequency_response(b, a, title):
    w, h = freqz(b, a)
    plt.plot(w, 20 * np.log10(np.maximum(abs(h), 1e-10)))  # Avoid log(0) issue
    plt.title(f'{title} Frequency Response')
    plt.xlabel('Frequency [radians / sample]')
    plt.ylabel('Amplitude [dB]')
    plt.grid()

# Plot poles and zeros
def plot_poles_zeros(b, a, title):
    zeros, poles, _ = tf2zpk(b, a)
    plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), color='red', label='Poles')
    plt.title(f'{title} Poles and Zeros')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid()

# Design and analyze filters
filter_types = ['lowpass', 'highpass', 'bandpass', 'bandstop']

plt.figure(figsize=(14, 14))

for i, filter_type in enumerate(filter_types):
    b, a = design_filter(filter_type)
    
    plt.subplot(len(filter_types), 2, 2*i + 1)
    plot_frequency_response(b, a, filter_type.capitalize())
    
    plt.subplot(len(filter_types), 2, 2*i + 2)
    plot_poles_zeros(b, a, filter_type.capitalize())

plt.tight_layout()
plt.show()
