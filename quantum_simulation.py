"""evolution of a Gaussian wave packet using the time-dependent 
Schrödinger equation."""

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Constants
# hbar = 1  # Reduced Planck's constant
# m = 1  # Mass of the particle
# L = 10  # Length of the box
# N = 200  # Number of points
# dx = L / N
# dt = 0.01  # Time step

# # Spatial grid
# x = np.linspace(-L/2, L/2, N)
# k0 = 5  # Initial wave number

# # Initial Gaussian wave packet (real and imaginary parts)
# psi_real = np.exp(-x**2) * np.cos(k0 * x)
# psi_imag = np.exp(-x**2) * np.sin(k0 * x)

# # Laplacian operator (numerical second derivative)
# def laplacian(psi):
#     return (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / dx**2

# # Plot setup
# fig, ax = plt.subplots()
# ax.set_xlim(-L/2, L/2)
# ax.set_ylim(0, 1)
# line, = ax.plot(x, psi_real**2 + psi_imag**2, 'b', lw=2)

# # Animation update function
# def update(frame):
#     global psi_real, psi_imag
#     psi_real += -hbar * laplacian(psi_imag) * dt / (2 * m)
#     psi_imag += hbar * laplacian(psi_real) * dt / (2 * m)
    
#     # Update wave function probability
#     line.set_ydata(psi_real**2 + psi_imag**2)
#     return line,

# # Create animation
# ani = animation.FuncAnimation(fig, update, frames=2000, interval=50, blit=False)

# # Ensure proper animation display
# plt.pause(0.1)
# plt.show()


"""Gaussian wave packet evolving under the free Schrödinger equation.
np.fft.fftfreq(N, dx) → Generates an array of frequencies for Fourier transforms.
Multiply by 2π →frequency to wave number
np.fft.fft(psi)→Fourier transform to get the momentum-space wave function
np.fft.ifft(...) → Transforms back to position space."""

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Define grid
# N = 256
# L = 10.0
# x = np.linspace(-L, L, N)
# dx = x[1] - x[0]
# k = np.fft.fftfreq(N, dx) * 2 * np.pi

# # Initial wave packet
# x0, sigma, k0 = -2.0, 0.5, 5.0
# psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
# psi_k = np.fft.fft(psi)

# # Time evolution
# dt, frames = 0.05, 100
# fig, ax = plt.subplots()
# line, = ax.plot(x, np.abs(psi)**2, 'r', lw=2)
# ax.set_xlim(-L, L)
# ax.set_ylim(0, 1)

# def update(n):
#     global psi_k
#     psi_t = np.fft.ifft(psi_k * np.exp(-1j * (k**2) * dt * n / 2))
#     line.set_ydata(np.abs(psi_t)**2)
#     return line,

# ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)
# plt.show()


"""Plotting wavefunctions for the first few quantum states in a 
harmonic oscillator."""

# from scipy.special import hermite
# from scipy.constants import hbar, m_e
# import numpy as np
# import matplotlib.pyplot as plt

# # Define potential
# x = np.linspace(-4, 4, 500)
# V = 0.5 * x**2

# # Compute wavefunctions
# def psi(n, x):
#     return np.exp(-x**2/2) * hermite(n)(x) / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi))

# # Plot energy levels and wavefunctions
# plt.figure(figsize=(7,5))
# for n in range(4):   #Loops over quantum numbers 
#     plt.plot(x, psi(n, x) + n, label=f'n={n}')  

# plt.plot(x, V, 'k--', label="Potential")
# plt.xlabel('Position')
# plt.ylabel('Energy')
# plt.legend()
# plt.title("Quantum Harmonic Oscillator Wavefunctions")
# plt.show()


"""Simulating a double-slit experiment using Fresnel-Kirchhoff 
diffraction theory."""

# import numpy as np
# import matplotlib.pyplot as plt
# # Define parameters
# wavelength = 500e-9  # 500 nm light
# d = 5e-6  # Slit separation
# L = 1  # Distance to screen
# x = np.linspace(-1e-2, 1e-2, 1000)
# # Compute intensity pattern
# theta = np.arctan(x / L)
# beta = np.pi * d * np.sin(theta) / wavelength
# I = (np.cos(beta))**2
# # Plot
# plt.figure(figsize=(8,4))
# plt.plot(x*1e3, I, 'b', lw=2)
# plt.xlabel("Screen position (mm)")
# plt.ylabel("Intensity")
# plt.title("Double-Slit Interference Pattern")
# plt.show()


"""Simulating wave packet tunneling through a potential barrier
 using Crank-Nicolson method."""

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Grid settings
# N = 400
# L = 10.0
# x = np.linspace(-L, L, N)
# dx = x[1] - x[0]
# dt = 10

# # Initial wave packet
# x0, sigma, k0 = -5.0, 0.5, 5.0
# psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
# psi /= np.sqrt(np.sum(np.abs(psi)**2))

# # Potential barrier
# V = np.zeros_like(x)
# V[N//2-10:N//2+10] = 10.0

# # Animation
# fig, ax = plt.subplots()
# line, = ax.plot(x, np.abs(psi)**2, 'r', lw=2)
# ax.set_xlim(-L, L)
# ax.set_ylim(0, 1)

# def update(n):
#     global psi
#     psi = psi * np.exp(-1j * dt * V)
#     line.set_ydata(np.abs(psi)**2)
#     return line,

# ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
# plt.show()


"""Visualizing a single qubit state evolution on the Bloch sphere."""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

# Define Bloch sphere
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='c', alpha=0.3)

# Define qubit evolution
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

def update(n):
    ax.clear()
    ax.plot_surface(x, y, z, color='c', alpha=0.3)
    ax.quiver(0, 0, 0, np.sin(theta[n])*np.cos(phi[n]), np.sin(theta[n])*np.sin(phi[n]), np.cos(theta[n]), color='r', lw=3)
    return ax,

ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()


