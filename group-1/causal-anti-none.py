import numpy as np
import matplotlib.pyplot as plt

# Time interval for the noncausal signal
t_noncausal = np.linspace(-1, 1, 1000)

# Causal Signal: x(t) = e^{-5t}u(t)
t_causal = np.linspace(0, 1, 1000)
causal_signal = np.exp(-5 * t_causal)

# Anticausal Signal: x(t) = e^{5t}u(-t)
t_anticausal = np.linspace(-1, 0, 1000)
anticausal_signal = np.exp(5 * t_anticausal)

# Noncausal Signal: x(t) = e^{-t^2}
noncausal_signal = np.exp(-t_noncausal**2)

# Plot Causal, Anticausal, and Noncausal Signals
plt.figure(figsize=(10, 6))

plt.plot(t_causal, causal_signal, label='Causal Signal ($e^{-5t}u(t)$)')
plt.plot(t_anticausal, anticausal_signal, label='Anticausal Signal ($e^{5t}u(-t)$)')
plt.plot(t_noncausal, noncausal_signal, label='Noncausal Signal ($e^{-t^2}$)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Causal, Anticausal, and Noncausal Signals')
plt.legend()
plt.grid(True)

plt.show()
