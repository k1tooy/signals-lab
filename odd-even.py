import numpy as np
import matplotlib.pyplot as plt

# Time interval
t = np.linspace(0, 1, 1000)

# Even Signal: x(t) = cos(2π4t)
even_signal = np.cos(2 * np.pi * 4 * t)

# Odd Signal: x(t) = sin(2π4t)
odd_signal = np.sin(2 * np.pi * 4 * t)

# Plot Even and Odd Signals
plt.figure(figsize=(10, 6))

plt.plot(t, even_signal, label='Even Signal ($\cos(2\pi 4t)$)')
plt.plot(t, odd_signal, label='Odd Signal ($\sin(2\pi 4t)$)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Even and Odd Signals')
plt.legend()
plt.grid(True)

plt.show()
