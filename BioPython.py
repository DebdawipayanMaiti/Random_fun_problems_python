
"""
BioPython.py

This script contains multiple simulations and models from computational biology:
1. Genetic Drift Simulation
2. Michaelis-Menten Enzyme Kinetics
3. Lotka-Volterra Predator-Prey Dynamics
4. Needleman-Wunsch Sequence Alignment

Each section is well-commented to explain the biological context and Python implementation.
"""

import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from scipy.integrate import odeint  # Import function to solve ODEs


# -----------------------------------------------
# 1. Genetic Drift Simulation
# -----------------------------------------------
def genetic_drift(N, p_A, generations):
    """
    Simulates genetic drift over generations.

    Parameters:
    N : int
        Population size
    p_A : float
        Initial allele frequency of 'A'
    generations : int
        Number of generations to simulate

    Returns:
    list
        Allele frequencies over generations
    """
    p_values = [p_A]
    for _ in range(generations):
        p_A = np.random.binomial(N, p_A) / N
        p_values.append(p_A)
        if p_A == 0 or p_A == 1:
            break
    return p_values

# Parameters for genetic drift
N = 100
p_A = 0.5
generations = 100
p_values = genetic_drift(N, p_A, generations)

# Plot genetic drift
plt.figure()
plt.plot(p_values, marker='o', linestyle='-')
plt.xlabel("Generations")
plt.ylabel("Allele Frequency of A")
plt.title("Genetic Drift Simulation")
plt.grid(True)
plt.show()


# -----------------------------------------------
# 2. Michaelis-Menten Enzyme Kinetics
# -----------------------------------------------
def michaelis_menten(S, Vmax, Km):
    """
    Calculates reaction rate using Michaelis-Menten kinetics.

    Parameters:
    S : array-like
        Substrate concentrations
    Vmax : float
        Maximum reaction rate
    Km : float
        Michaelis constant

    Returns:
    array
        Reaction rates
    """
    return (Vmax * S) / (Km + S)

S = np.linspace(0, 10, 100)
Vmax = 10
Km = 2
V = michaelis_menten(S, Vmax, Km)

# Plot Michaelis-Menten kinetics
plt.figure()
plt.plot(S, V, label="Michaelis-Menten Curve")
plt.xlabel("Substrate Concentration [S]")
plt.ylabel("Reaction Rate (v)")
plt.title("Michaelis-Menten Enzyme Kinetics")
plt.legend()
plt.grid(True)
plt.show()


# -----------------------------------------------
# 3. Lotka-Volterra Predator-Prey Model
# -----------------------------------------------
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    """
    Defines Lotka-Volterra equations for predator-prey dynamics.

    Parameters:
    y : list
        Populations [prey, predator]
    t : float
        Time
    alpha, beta, delta, gamma : float
        Model parameters

    Returns:
    list
        Derivatives [dPrey/dt, dPredator/dt]
    """
    P, R = y
    dPdt = alpha * P - beta * P * R
    dRdt = delta * P * R - gamma * R
    return [dPdt, dRdt]

# Model parameters
alpha, beta, delta, gamma = 0.1, 0.02, 0.01, 0.1
y0 = [40, 9]  # Initial populations
t = np.linspace(0, 200, 1000)
solution = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma))
P, R = solution.T

# Plot predator-prey dynamics
plt.figure()
plt.plot(t, P, label="Prey Population", color='blue')
plt.plot(t, R, label="Predator Population", color='red')
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Predator-Prey Model (Lotka-Volterra)")
plt.legend()
plt.grid(True)
plt.show()


# -----------------------------------------------
# 4. Needleman-Wunsch Sequence Alignment
# -----------------------------------------------
def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """
    Implements the Needleman-Wunsch algorithm for global sequence alignment.

    Parameters:
    seq1, seq2 : str
        DNA sequences
    match : int
        Score for a match
    mismatch : int
        Score for a mismatch
    gap : int
        Gap penalty

    Returns:
    ndarray
        Alignment score matrix
    """
    len1, len2 = len(seq1), len(seq2)
    score_matrix = np.zeros((len1 + 1, len2 + 1))

    # Initialize first row and column
    for i in range(len1 + 1):
        score_matrix[i][0] = i * gap
    for j in range(len2 + 1):
        score_matrix[0][j] = j * gap

    # Fill score matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            match_score = match if seq1[i - 1] == seq2[j - 1] else mismatch
            score_matrix[i][j] = max(
                score_matrix[i - 1][j - 1] + match_score,
                score_matrix[i - 1][j] + gap,
                score_matrix[i][j - 1] + gap
            )
    return score_matrix

# DNA sequence example
seq1 = "GATTACA"
seq2 = "GCATGCU"
alignment_matrix = needleman_wunsch(seq1, seq2)

# Print the alignment matrix
print("Alignment Score Matrix:")
print(alignment_matrix)
