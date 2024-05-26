import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, dimpulse, dlti, residue, tf2zpk

# Define a discrete-time signal
n = np.arange(0, 10)
x = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1, 0])

# Define the transfer function coefficients for demonstration
b = [1, -1.5, 0.7]  # Numerator coefficients
a = [1, -0.9, 0]    # Denominator coefficients padded to make lengths equal

# Compute the Z-transform (frequency response) using freqz
w, h = freqz(b, a)

# Compute the inverse Z-transform using residue method
r, p, k = residue(b, a)
system = dlti(b, a)
t, imp_response = dimpulse(system, n=len(n))

# Plot the results
plt.figure(figsize=(14, 10))

# Plot the original discrete-time signal
plt.subplot(2, 2, 1)
plt.stem(n, x)
plt.title('Original Discrete-Time Signal')
plt.xlabel('n')
plt.ylabel('x[n]')

# Plot the Z-transform (magnitude response)
plt.subplot(2, 2, 2)
plt.plot(w, np.abs(h))
plt.title('Z-Transform Magnitude Response')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(z)|')

# Plot the inverse Z-transform (impulse response)
plt.subplot(2, 2, 3)
plt.stem(n, np.real(imp_response[0][:len(n)]))
plt.title('Inverse Z-Transform (Impulse Response)')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot poles and zeros in the Z-plane
zeros, poles, _ = tf2zpk(b, a)

plt.subplot(2, 2, 4)
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Poles')
plt.title('Poles and Zeros in Z-plane')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

