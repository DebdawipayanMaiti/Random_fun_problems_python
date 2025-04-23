"""
stochastic_process_bio.py

This script implements simulations of several stochastic processes in biology:
1. Random Walk to model protein diffusion in membranes
2. Stochastic gene expression with state toggling
3. Stochastic SIR epidemic model using Gillespie’s algorithm
4. Genetic drift simulation in small populations
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. 2D Random Walk - Protein Lateral Diffusion in Membranes
# ---------------------------------------------------------

# Simulation parameters
n_steps = 1000         # Total time steps for each particle
n_particles = 100      # Number of protein particles

# Initialize positions for each particle: shape (particles, steps, 2D)
positions = np.zeros((n_particles, n_steps, 2))

# Simulate random walk
for i in range(1, n_steps):
    # Each particle takes a step randomly in x and y direction: ±1
    steps = np.random.choice([-1, 1], size=(n_particles, 2))
    positions[:, i, :] = positions[:, i - 1, :] + steps

# Compute mean squared displacement (MSD)
msd = np.mean(np.sum(positions**2, axis=2), axis=0)

# Plot MSD vs time
plt.figure()
plt.plot(range(n_steps), msd)
plt.xlabel("Time Step")
plt.ylabel("Mean Squared Displacement (MSD)")
plt.title("Random Walk - MSD vs Time")
plt.grid(True)
plt.show()


# ---------------------------------------------------------
# 2. Stochastic Gene Expression (Two-State Model)
# ---------------------------------------------------------

# Parameters for gene switching and mRNA dynamics
k_on = 0.1       # Probability rate of switching ON
k_off = 0.05     # Probability rate of switching OFF
k_mRNA = 2       # mRNA production rate (when gene is ON)
decay = 0.1      # mRNA degradation rate
T = 1000         # Total simulation steps

# Initialization
state = 0               # Start in OFF state (0)
mRNA_count = 0
states = []             # Track gene state over time
mRNA_counts = []        # Track mRNA levels over time

# Simulate gene expression
for t in range(T):
    # Toggle state based on stochastic switch
    if state == 0 and np.random.rand() < k_on:
        state = 1
    elif state == 1 and np.random.rand() < k_off:
        state = 0

    # Stochastic mRNA production and degradation
    if state == 1:
        mRNA_count += np.random.poisson(k_mRNA)
    mRNA_count -= np.random.poisson(decay * mRNA_count)
    mRNA_count = max(mRNA_count, 0)  # Prevent negative count

    states.append(state)
    mRNA_counts.append(mRNA_count)

# Plot gene state and mRNA over time
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(states, label="Gene State (0=OFF, 1=ON)")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(mRNA_counts, label="mRNA Count")
plt.legend()
plt.xlabel("Time")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 3. Stochastic SIR Model using Gillespie's Algorithm
# ---------------------------------------------------------

# Define parameters
beta = 0.3       # Infection rate
gamma = 0.1      # Recovery rate
N = 1000         # Total population size

# Initial population counts: one infected, rest susceptible
S, I, R = N - 1, 1, 0

# Set maximum simulation time
Tmax = 100

# Initialize time and data tracking lists
t = 0
times = [t]
S_list = [S]
I_list = [I]
R_list = [R]

# Run simulation while infection persists and time is within limits
while I > 0 and t < Tmax:
    rate_infect = beta * S * I / N          # Infection event rate
    rate_recover = gamma * I                # Recovery event rate
    total_rate = rate_infect + rate_recover # Total event rate

    if total_rate == 0:
        break  # No events possible

    # Time to next event, exponentially distributed
    t += np.random.exponential(1 / total_rate)

    # Decide which event occurs based on relative rates
    if np.random.rand() < rate_infect / total_rate:
        S -= 1  # One person gets infected
        I += 1
    else:
        I -= 1  # One person recovers
        R += 1

    # Record current state
    times.append(t)
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot SIR dynamics over time
plt.figure()
plt.plot(times, S_list, label="Susceptible")
plt.plot(times, I_list, label="Infected")
plt.plot(times, R_list, label="Recovered")
plt.xlabel("Time")
plt.ylabel("Population Count")
plt.legend()
plt.title("Stochastic SIR Model")
plt.grid(True)
plt.show()


# ---------------------------------------------------------
# 4. Genetic Drift Simulation
# ---------------------------------------------------------

# Set genetic drift parameters
N = 100          # Diploid population size
p = 0.5          # Initial allele frequency of A
generations = 100

# Store allele frequency at each generation
allele_frequencies = [p]

# Simulate drift over generations
for _ in range(generations):
    # Sample allele counts from binomial distribution (2N alleles)
    p = np.random.binomial(2 * N, p) / (2 * N)
    allele_frequencies.append(p)

# Plot allele frequency changes over time
plt.figure()
plt.plot(range(generations + 1), allele_frequencies, marker="o")
plt.xlabel("Generations")
plt.ylabel("Allele Frequency")
plt.title("Genetic Drift Simulation")
plt.ylim(0, 1)
plt.grid(True)
plt.show()
'''


