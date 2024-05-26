import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the discrete signals
x_discrete = np.array([1, 2, 3])
h_discrete = np.array([1, 1, 1])

# Discrete convolution using numpy
y_discrete = np.convolve(x_discrete, h_discrete)

# Manual continuous convolution function
def x_continuous(t):
    return np.exp(-t) if t >= 0 else 0

def h_continuous(t):
    return 1 if t >= 0 else 0

def continuous_convolution(x, h, t):
    integrand = lambda tau: x(tau) * h(t - tau)
    result, _ = quad(integrand, -np.inf, np.inf)
    return result

# Evaluate continuous convolution at specific points
t_values = np.linspace(0, 10, 100)
y_continuous = [continuous_convolution(x_continuous, h_continuous, t) for t in t_values]

# Frequency domain convolution using FFT
n = len(x_discrete) + len(h_discrete) - 1
X = np.fft.fft(x_discrete, n)
H = np.fft.fft(h_discrete, n)
Y = X * H
y_fft = np.fft.ifft(Y)

# Plotting the results
plt.figure(figsize=(15, 5))

# Plot discrete convolution
plt.subplot(1, 3, 1)
plt.stem(np.arange(len(y_discrete)), y_discrete)
plt.title('Discrete Convolution')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot continuous convolution
plt.subplot(1, 3, 2)
plt.plot(t_values, y_continuous)
plt.title('Continuous Convolution')
plt.xlabel('t')
plt.ylabel('Amplitude')

# Plot frequency domain convolution
plt.subplot(1, 3, 3)
plt.stem(np.arange(len(y_fft)), np.real(y_fft))
plt.title('Frequency Domain Convolution (FFT)')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

