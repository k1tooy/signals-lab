import numpy as np
import matplotlib.pyplot as plt

# Time interval
t = np.linspace(0, 1, 1000)

# Periodic Signal: Square wave with a frequency of 5 Hz
periodic_signal = 0.5 * (np.sign(np.sin(2 * np.pi * 5 * t)) + 1)

# Aperiodic Signal: x(t) = e^{-5t}
aperiodic_signal = np.exp(-5 * t)

# Plot Periodic vs. Aperiodic Signals
plt.figure(figsize=(10, 6))

plt.plot(t, periodic_signal, label='Periodic Signal (5 Hz Square Wave)')
plt.plot(t, aperiodic_signal, label='Aperiodic Signal ($e^{-5t}$)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Periodic vs. Aperiodic Signals')
plt.legend()
plt.grid(True)

plt.show()

