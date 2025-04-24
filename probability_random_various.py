#### Random module tutoeial
# import random
# fruits = ['apple', 'banana', 'cherry']
# print(random.random()) # random float between 0.0 and 1.0 
# print(random.randint(1, 10)) # integer between a and b (inclusive).
# print(random.uniform(1.5, 5.5)) # float between a and b.
# print(random.choice(fruits)) # randomly selected element from a sequence
# print(random.choices(fruits, k=2)) # Returns a list of k elements chosen from a population with optional weights (i.e., biased selection).
# print(random.shuffle(xor))
# x = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# random.shuffle(x) # Shuffles the elements of a list in place.
# print(x)
# print(random.sample(range(1, 100), 5)) # Returns a k-length list of unique elements chosen from a population.
# print(random.gauss(0, 1)) # Returns a random number from a Gaussian (normal) distribution with mean mu and standard deviation sigma.
# print(random.betavariate(2,3)) # Returns a random number based on the Beta distribution with parameters alpha and beta.
# random.seed(10) # Initializes the random number generator with a seed value a. This ensures reproducibility if the same seed is used.
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
# x = np.linspace(-5, 5, 1000)  # Range of x values
# y = norm.pdf(x, 0, 1)        # Normal distribution PDF (mean=0, std=1)
# plt.plot(x, y)
# plt.show()


#####all from numpy
x = random.randint(100) # Generate a random integer from 0 to 100:
x = random.rand() # Generate a random float from 0 to 1x=random.randint(100, size=(5))
x = random.randint(100, size=(5)) # Generate a 1-D array containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5)) # 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.rand(5) # 1-D array containing 5 random floats:
x = random.rand(3, 5) # 2-D array with 3 rows, each row containing 5 random numbers:
x = random.choice([3, 5, 7, 9]) # generate a random value based on an array of values.
x = random.choice([3, 5, 7, 9], size=(3, 5)) #  2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

"""Simulate rolling two six-sided dice 10,000 times, and then plot the probability distribution of the sum of the two dice."""

# import random
# import matplotlib.pyplot as plt
# # Simulate rolling two dice 10,000 times
# rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10000)]
# # Count occurrences of each possible sum (2 to 12)
# counts = {sum_: rolls.count(sum_) for sum_ in range(2, 13)}
# # Convert counts to probabilities
# total_rolls = sum(counts.values())
# probs = [counts[sum_] / total_rolls for sum_ in range(2, 13)]
# # Plotting
# plt.bar(range(2, 13), probs, color='skyblue', edgecolor='black')
# plt.xticks(range(2, 13))
# plt.xlabel('Sum of Two Dice')
# plt.ylabel('Probability')
# plt.title('Probability Distribution of Two Dice Sums (10,000 Rolls)')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
# print(rolls)
# print(counts)
# print(probs)

"""You have a biased coin, where the probability of getting heads is p = 0.7 and the probability of getting tails is 1 - p = 0.3. 
Simulate 1000 coin tosses and plot the cumulative number of heads and tails over time.
Requirements: Simulate 1000 biased coin tosses.Track the cumulative number of heads and tails after each toss.
Plot both the number of heads and the number of tails over time on the same graph."""
# import random
# import matplotlib.pyplot as plt
# # Settings
# tosses = 1000
# p_heads = 0.7
# # Track results
# heads, tails = 0, 0
# heads_list, tails_list = [], []
# # Simulate tosses
# for _ in range(tosses):
#     if random.random() < p_heads:
#         heads += 1
#     else:
#         tails += 1
#     heads_list.append(heads)
#     tails_list.append(tails)
# # Plot
# plt.plot(range(tosses), heads_list, label='Heads', color='blue')
# plt.plot(range(tosses), tails_list, label='Tails', color='orange')
# plt.xlabel('Number of Tosses')
# plt.ylabel('Cumulative Count')
# plt.title('Biased Coin Toss Simulation (P(Heads) = 0.7)')
# plt.legend()
# plt.grid(True)
# plt.show()

"""Consider a random walk in a 2D plane, where at each step, you move randomly in one of the four cardinal 
directions (North, South, East, or West). However, there is a drift that biases the movement: there is a higher
probability of moving East (0.4 probability), North (0.3 probability), South (0.2 probability), and West (0.1 probability).
Simulate this random walk for 1000 steps and plot the path the walker takes on the 2D grid."""

# import random
# import matplotlib.pyplot as plt
# # Define probabilities for directions: East, North, South, West
# directions = ['E', 'N', 'S', 'W']
# probabilities = [0.4, 0.3, 0.2, 0.1]
# # Direction vectors
# move_map = {
#     'E': (1, 0),
#     'N': (0, 1),
#     'S': (0, -1),
#     'W': (-1, 0)
# }
# # Initialize position
# x, y = 0, 0
# path_x, path_y = [x], [y]
# # Perform 1000 steps
# for _ in range(10):
#     move = random.choices(directions, probabilities)[0]
#     dx, dy = move_map[move]
#     x += dx
#     y += dy
#     path_x.append(x)
#     path_y.append(y)
# # Plotting
# plt.figure(figsize=(8, 6))
# plt.plot(path_x, path_y, color='blue')
# plt.scatter(path_x[0], path_y[0], color='green', label='Start', zorder=5)
# plt.scatter(path_x[-1], path_y[-1], color='red', label='End', zorder=5)
# plt.title("2D Random Walk with Drift")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# plt.legend()
# plt.axis("equal")
# plt.show()

"""In the birthday paradox, you calculate the probability that two people in a group of n have the same birthday. 
This probability increases rapidly as the number of people grows. Simulate this for groups of varying sizes 
(from 2 to 100 people) and plot the probability that at least two people share the same birthda"""

# import random
# import matplotlib.pyplot as plt
# # Function to simulate birthday paradox for a group of 'n' people
# def birthday_paradox(n):
#     # Generate random birthdays (represented by numbers 0-364, corresponding to days of the year)
#     birthdays = [random.randint(0, 364) for _ in range(n)]
#     # Check if there are any duplicates (i.e., two people share the same birthday)
#     return len(birthdays) != len(set(birthdays))
# # Simulate for groups from 2 to 100 people
# group_sizes = list(range(2, 101))
# probabilities = []
# # Perform the simulation 1000 times for each group size
# for n in group_sizes:
#     matches = sum(birthday_paradox(n) for _ in range(1000))
#     probabilities.append(matches / 1000)
# # Plot the results
# plt.plot(group_sizes, probabilities, marker='o', color='b')
# plt.title('Birthday Paradox Simulation')
# plt.xlabel('Group Size (n)')
# plt.ylabel('Probability of Shared Birthday')
# plt.grid(True)
# plt.show()

"""Estimate the mean of a population of numbers by taking random samples. Simulate drawing 100 samples from a 
population of size 1000 and plot how the sample mean approaches the population mean as more samples are taken.
Create a population of 1000 random numbers (e.g., uniformly distributed between 0 and 100).
Take random samples of size 10, 20, 50, and 100, and calculate the mean for each sample.
Plot the sample mean as a function of the number of samples taken.
Compare how the sample mean converges to the true population mean as the number of samples increases."""

# import random
# import numpy as np
# import matplotlib.pyplot as plt
# # Step 1: Create a population of 1000 random numbers (uniform distribution between 0 and 100)
# population = [random.uniform(0, 100) for _ in range(1000)]
# population_mean = np.mean(population)
# # Step 2: Function to draw random samples and calculate the mean
# def estimate_sample_mean(sample_size, num_samples):
#     sample_means = []
#     for _ in range(num_samples):
#         sample = random.sample(population, sample_size)
#         sample_mean = np.mean(sample)
#         sample_means.append(sample_mean)
#     return sample_means
# # Step 3: Simulate drawing samples of increasing size
# sample_sizes = [10, 20, 50, 100]
# num_samples = 100  # Number of samples for each sample size
# # Step 4: Plot the sample mean as the sample size increases
# plt.figure(figsize=(10, 6))
# for size in sample_sizes:
#     sample_means = estimate_sample_mean(size, num_samples)
#     plt.plot(range(num_samples), sample_means, label=f'Sample size = {size}')
# # Step 5: Add population mean line to the plot
# plt.axhline(y=population_mean, color='red', linestyle='--', label='Population Mean')
# # Step 6: Customize the plot
# plt.title('Estimation of Population Mean Using Random Sampling')
# plt.xlabel('Number of Samples')
# plt.ylabel('Sample Mean')
# plt.legend()
# plt.grid(True)
# # Step 7: Show the plot
# plt.show()

"""Simulate drawing cards from a shuffled deck of 52 cards. After each draw, plot the number of red cards 
(hearts and diamonds) and black cards (clubs and spades) drawn so far."""

import random
import matplotlib.pyplot as plt
# Step 1: Define the deck of cards
# A deck contains 26 red cards (hearts and diamonds) and 26 black cards (clubs and spades)
deck = ['red'] * 26 + ['black'] * 26
# Step 2: Shuffle the deck
random.shuffle(deck)
# Step 3: Initialize counters for red and black cards
red_count = 0
black_count = 0
# Step 4: Lists to track the number of red and black cards drawn over time
red_counts = []
black_counts = []
# Step 5: Draw cards one by one and count red and black cards
for card in deck:
    if card == 'red':
        red_count += 1
    else:
        black_count += 1
    
    # Append the current counts to the lists
    red_counts.append(red_count)
    black_counts.append(black_count)
# Step 6: Plot the number of red and black cards drawn over time
plt.figure(figsize=(10, 6))
plt.plot(range(52), red_counts, label='Red Cards', color='red')
plt.plot(range(52), black_counts, label='Black Cards', color='black')
# Step 7: Customize the plot
plt.title('Card Deck Simulation: Red vs. Black Cards')
plt.xlabel('Number of Cards Drawn')
plt.ylabel('Count of Cards')
plt.legend()
plt.grid(True)
# Step 8: Show the plot
plt.show()



"""1. "Zombie Apocalypse" Simulation
In a 2D world, one human (blue dot) starts at (0,0) and 5 zombies (red dots) are scattered randomly in a 100x100 grid. Every turn, the human moves randomly (one step in one of 4 directions: N/S/E/W), and zombies move toward the human by one unit (whichever direction reduces distance).

The game ends when a zombie reaches the human (same position), or 500 turns pass. Plot the human and zombie paths. Mark the caught point with a black X if caught.

Add twist: Human has a 10% chance of getting a "speed boost" (moves two steps that turn).
"""

import random
import matplotlib.pyplot as plt

human_x = 0
human_y = 0
zombie_x = [random.randint(-50, 50) for _ in range(5)]
zombie_y = [random.randint(-50, 50) for _ in range(5)]

human_x_path = [human_x]
human_y_path = [human_y]
zombie_x_paths = [[zombie_x[i]] for i in range(5)]
zombie_y_paths = [[zombie_y[i]] for i in range(5)]

caught = False

for t in range(500):
    speed = 2 if random.random() < 0.1 else 1
    move = random.choice(["N", "S", "E", "W"])
    if move == "N":
        human_y += speed
    elif move == "S":
        human_y -= speed
    elif move == "E":
        human_x += speed
    elif move == "W":
        human_x -= speed

    human_x_path.append(human_x)
    human_y_path.append(human_y)

    for i in range(5):
        if zombie_x[i] < human_x:
            zombie_x[i] += 1
        elif zombie_x[i] > human_x:
            zombie_x[i] -= 1

        if zombie_y[i] < human_y:
            zombie_y[i] += 1
        elif zombie_y[i] > human_y:
            zombie_y[i] -= 1

        zombie_x_paths[i].append(zombie_x[i])
        zombie_y_paths[i].append(zombie_y[i])

        if zombie_x[i] == human_x and zombie_y[i] == human_y:
            caught = True
            caught_index = i
            break

    if caught:
        break

plt.plot(human_x_path, human_y_path, 'b-', label="Human")
for i in range(5):
    plt.plot(zombie_x_paths[i], zombie_y_paths[i], '--', label="Zombie " + str(i+1))
if caught:
    plt.text(human_x, human_y, "Caught!", fontsize=12, color='red')
plt.legend()
plt.grid()
plt.title("Zombie Apocalypse")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


"""2. "Wandering Fish in a Pond"
A fish swims in a circular pond (radius 50 units). It starts at the center. Each turn it picks a random angle and moves 5 meters in that direction.

If it reaches or crosses the boundary of the pond, it "bounces" off the wall (reverse direction).

Simulate 300 turns, track its path, and plot the entire swimming trajectory.

Add twist: Every 50 turns, it gets hungry and swims twice the normal speed.


"""

import random
import math
import matplotlib.pyplot as plt

x = 0
y = 0
x_list = [x]
y_list = [y]
radius = 50

for t in range(300):
    angle = random.uniform(0, 2 * 3.14159)
    if t % 50 == 0 and t != 0:
        step = 10
    else:
        step = 5

    next_x = x + step * math.cos(angle)
    next_y = y + step * math.sin(angle)

    if math.sqrt(next_x**2 + next_y**2) > radius:
        angle += 3.14159  # reverse
        next_x = x + step * math.cos(angle)
        next_y = y + step * math.sin(angle)

    x = next_x
    y = next_y
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list, 'b-')
circle = plt.Circle((0, 0), radius, fill=False, color='gray', linestyle='--')
plt.gca().add_patch(circle)
plt.axis("equal")
plt.grid()
plt.title("Fish in Pond")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


###Monday Group Class test

# import random
# import matplotlib.pyplot as plt
# # Start point
# x = 0
# y = 5
# x_vals = [x]
# y_vals = [y]
# for i in range(20):
#     coin1 = random.choice(['H', 'T'])
#     coin2 = random.choice(['H', 'T'])
#     if coin1 == 'T' and coin2 == 'T':
#         y += 5
#     elif coin1 == 'H' and coin2 == 'T':
#         y += 10
#     elif coin1 == 'T' and coin2 == 'H':
#         y -= 5
#     else:  # (H, H)
#         y -= 10
#     x += 5
#     x_vals.append(x)
#     y_vals.append(y)
# plt.plot(x_vals, y_vals, marker='o',color='r')
# plt.title("Bikers' Journey")
# plt.xlabel("East-West Distance (km)")
# plt.ylabel("North-South Position (km)")
# plt.show()







##Tuesday Group Class test

import random
import matplotlib.pyplot as plt

# Initial positions
tom_x, tom_y = 5, 5
jerry_x, jerry_y = 5, 10

# Store paths
tom_path_x = [tom_x]
tom_path_y = [tom_y]
jerry_path_x = [jerry_x]
jerry_path_y = [jerry_y]

# Max turns
max_turns = 1000

winner = None

for turn in range(1, max_turns + 1):
    # Tom's move: coin toss
    if random.random() < 0.5:  # Head
        tom_x += 10
    # else Tail: tom_x stays the same
    tom_path_x.append(tom_x)
    tom_path_y.append(tom_y)  # y stays the same

    # Jerry's move: roll die
    roll = random.randint(1, 6)
    if roll == 1:
        jerry_x += 5
    elif roll == 2:
        jerry_x += 10
    elif roll == 3:
        jerry_y += 5
    elif roll == 4:
        jerry_y -= 5
    elif roll == 5:
        jerry_x += 5
        jerry_y += 5
    elif roll == 6:
        jerry_x += 5
        jerry_y -= 5

    jerry_path_x.append(jerry_x)
    jerry_path_y.append(jerry_y)

    # Check for victory
    if tom_x >= 100 or jerry_x >= 100:
        if tom_x >= 100 and jerry_x >= 100:
            if tom_x > jerry_x:
                winner = "Tom wins!"
            elif jerry_x > tom_x:
                winner = "Jerry wins!"
            else:
                winner = "Both win!"
        elif tom_x >= 100:
            winner = "Tom wins!"
        elif jerry_x >= 100:
            winner = "Jerry wins!"
        break

if not winner:
    winner = "None wins!"

# Plot
plt.figure(figsize=(12, 6))
plt.plot(tom_path_x, tom_path_y, 'b-o', label='Tom', linewidth=2, markersize=3)
plt.plot(jerry_path_x, jerry_path_y, 'r--s', label='Jerry', linewidth=2, markersize=3)
plt.axvline(x=100, color='green', linestyle=':', label='Finish Line')
plt.legend()
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('Tom vs Jerry Race Simulation')
plt.text(102, max(tom_y, jerry_y) + 2, winner, fontsize=12, color='purple')
plt.grid(True)
plt.show()


"""In a forest consisting of 1000 trees arranged in a grid, a fire starts at one 
randomly selected tree and spreads each minute to any of the four adjacent trees 
(up, down, left, right) with a probability of 0.4 per direction, provided the neighboring
 tree has not already burned; once a tree catches fire, it burns for exactly one minute 
 and is then considered completely burned and inert, unable to burn again or contribute 
 to the spread; your task is to simulate the fire's spread minute by minute, stopping 
 only when no burning trees remain, and report the total number of trees burned, the 
 maximum number of trees burning simultaneously at any moment, and the time at which the fire stops."""

# import random
# grid_size = 30  # 30x30 = 900 trees
# forest = [['T' for _ in range(grid_size)] for _ in range(grid_size)]
# burning = [(random.randint(0, grid_size-1), random.randint(0, grid_size-1))]
# forest[burning[0][0]][burning[0][1]] = 'F'
# time, burned = 0, 0
# while burning:
#     new_burning = []
#     for x, y in burning:
#         forest[x][y] = 'B'
#         burned += 1
#         for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < grid_size and 0 <= ny < grid_size and forest[nx][ny] == 'T':
#                 if random.random() < 0.4:
#                     forest[nx][ny] = 'F'
#                     new_burning.append((nx, ny))
#     burning = new_burning
#     time += 1

"""A company is trying to detect fraudulent financial transactions among 10,000 daily transactions, 
where each transaction has a 0.8% chance of being fraudulent, and each flagged transaction undergoes a 
review process with a 10% false negative rate and a 5% false positive rate; in addition, each fraudster 
who is not caught increases the chance of future frauds by 0.0002 per undetected fraud, representing 
adaptation in fraud strategies; simulate this process over 30 days, where each day you simulate all 
transactions, detect fraud, apply adaptive feedback to the fraud rate, and track the cumulative number 
of true positives, false positives, false negatives, and true negatives."""


# import random
# fraud_rate = 0.008
# days = 30
# results = {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}
# for _ in range(days):
#     transactions = [random.random() < fraud_rate for _ in range(10000)]

#     for is_fraud in transactions:
#         detected = random.random() >= 0.10 if is_fraud else random.random() < 0.05

#         if is_fraud and detected:
#             results['TP'] += 1
#         elif not is_fraud and detected:
#             results['FP'] += 1
#         elif is_fraud and not detected:
#             results['FN'] += 1
#         else:
#             results['TN'] += 1
#     fraud_rate += results['FN'] * 0.0002


"""In a city where 5000 households each consume a variable amount of electricity per day, modeled as a 
normal distribution with a mean of 12 kWh and a standard deviation of 3 kWh, a rolling blackout policy 
is triggered whenever total daily demand exceeds 60,000 kWh, causing 10% of households to be randomly cut 
off from power the next day, with a probability of 0.7 that they under-consume (50% of their mean) the following 
day due to awareness or caution; simulate 30 days of this policy in action, tracking total consumption, number 
of blackout-triggered days, the number of households affected, and how consumption trends shift over time due to adaptive behavior."""


# import random
# # Each of 5000 households starts with average usage ~12 kWh, plus some variation
# households = [12 + random.gauss(0, 3) for _ in range(5000)]
# # Keeps track of which households are in blackout mode
# blackout_list = set()
# # Stores daily total electricity usage
# consumption_log = []
# # Simulate for 30 days
# for day in range(30):
#     total_usage = 0
#     new_blackouts = set()
#     for i in range(5000):
#         if i in blackout_list:
#             # 70% of blackout households reduce future usage to 50%
#             if random.random() < 0.7:
#                 usage = households[i] * 0.5
#             else:
#                 usage = households[i]
#         else:
#             # Normal usage with random daily variation
#             usage = max(0, 12 + random.gauss(0, 3))
#         total_usage += usage
#     # If total usage exceeds limit, pick 10% of households for blackout
#     if total_usage > 60000:
#         blackout_list = set(random.sample(range(5000), 500))  # 10% of 5000
#     else:
#         blackout_list = set()
#     consumption_log.append(total_usage)
# # Print daily consumption for review
# for day, usage in enumerate(consumption_log, 1):
#     print(f"Day {day}: Total Usage = {usage:.2f} kWh")



"""A mobile game introduces a new in-game item with a loot box system where each player has a 5% chance
 of winning the item per box opened, but players become frustrated over time: after each failed attempt, 
 their probability of quitting the game increases by 1.5%, and if they quit, they do not return; simulate 
 10,000 players opening boxes until they either win the item or quit, and calculate the total number of players
 who obtained the item, the average number of boxes opened per player, and the distribution of quitting times 
 across the player base."""


# import random
# players = [{'got_item': False, 'quit': False, 'boxes': 0} for _ in range(10000)]
# for player in players:
#     quit_prob = 0
#     while not player['got_item'] and not player['quit']:
#         player['boxes'] += 1
#         if random.random() < 0.05:
#             player['got_item'] = True
#         else:
#             quit_prob += 0.015
#             if random.random() < quit_prob:
#                 player['quit'] = True
# got = sum(p['got_item'] for p in players)
# avg_boxes = sum(p['boxes'] for p in players) / len(players)



"""Two players, Alice and Bob, are playing a gambling game. Each turn, a player rolls a die. If the die lands 
on an even number, they gain points equal to the die roll. If it lands on an odd number, they lose points equal 
to the die roll. The game ends when a player reaches 100 points. Alternate turns between Alice and Bob until 
one player reaches 100 points. Track and plot the cumulative scores for both players at each turn."""
import matplotlib.pyplot as plt
import random

# # Initialize scores
# alice_score = 0
# bob_score = 0
# turns = []
# alice_scores = []
# bob_scores = []
# # Simulate the game
# turn = 0
# while alice_score < 100 and bob_score < 100:
#     if turn % 2 == 0:  # Alice's turn
#         roll = random.randint(1, 6)
#         if roll % 2 == 0:  # Even roll -> gain points
#             alice_score += roll
#         else:  # Odd roll -> lose points
#             alice_score -= roll
#         turns.append(turn)
#         alice_scores.append(alice_score)
#         bob_scores.append(bob_score)
#     else:  # Bob's turn
#         roll = random.randint(1, 6)
#         if roll % 2 == 0:
#             bob_score += roll
#         else:
#             bob_score -= roll
#         turns.append(turn)
#         alice_scores.append(alice_score)
#         bob_scores.append(bob_score)

#     turn += 1
# # Plot the scores
# plt.plot(turns, alice_scores, label='Alice')
# plt.plot(turns, bob_scores, label='Bob')
# plt.xlabel('Turn')
# plt.ylabel('Score')
# plt.title('Gambling Game: Alice vs Bob')
# plt.legend()
# plt.grid(True)
# plt.show()


""" Simulate a random walk in a 2D grid. Start at the origin (0, 0) and take steps in random directions 
(up, down, left, right). The walk continues until the walker hits a position it has already visited. 
Track the path of the walker and plot the journey."""
x, y = 0, 0
# visited_positions = {(x, y)}
# path_x, path_y = [x], [y]
# # Simulate the walk
# while True:
#     move = random.choice(['up', 'down', 'left', 'right'])
    
#     if move == 'up':
#         y += 1
#     elif move == 'down':
#         y -= 1
#     elif move == 'left':
#         x -= 1
#     elif move == 'right':
#         x += 1
    
#     if (x, y) in visited_positions:
#         break  # Stop if the position is revisited
#     visited_positions.add((x, y))
#     path_x.append(x)
#     path_y.append(y)
# # Plotting the random walk path
# plt.plot(path_x, path_y, marker='o', markersize=3, color='green')
# plt.title("Random Walk in 2D")
# plt.xlabel("X Position")
# plt.ylabel("Y Position")
# plt.grid(True)
# plt.show()

# # Parameters
# num_cells = 50
# num_genes = 4
# # Simulate gene expression for 4 genes across 50 cells (mean=10, std=2)
# gene_expression = np.random.normal(loc=10, scale=2, size=(num_cells, num_genes))
# # Calculate the mean expression per gene
# mean_expression = np.mean(gene_expression, axis=0)
# # Calculate the variance in expression per gene
# variance_expression = np.var(gene_expression, axis=0)
# # Plot mean expression per gene
# plt.figure(figsize=(10, 6))
# plt.bar(range(num_genes), mean_expression, color='skyblue', alpha=0.7)
# plt.xticks(range(num_genes), [f'Gene {i+1}' for i in range(num_genes)])
# plt.title('Mean Gene Expression per Gene', fontsize=14)
# plt.ylabel('Mean Expression Level', fontsize=12)
# plt.xlabel('Genes', fontsize=12)
# plt.tight_layout()
# plt.show()
# # Plot variance in expression per gene
# plt.figure(figsize=(10, 6))
# plt.bar(range(num_genes), variance_expression, color='salmon', alpha=0.7)
# plt.xticks(range(num_genes), [f'Gene {i+1}' for i in range(num_genes)])
# plt.title('Variance in Gene Expression per Gene', fontsize=14)
# plt.ylabel('Variance in Expression Level', fontsize=12)
# plt.xlabel('Genes', fontsize=12)
# plt.tight_layout()
# plt.show()
# # Apply KMeans clustering to group cells into two clusters based on gene expression
# kmeans = KMeans(n_clusters=2)
# cluster_labels = kmeans.fit_predict(gene_expression)
# # Visualize clustering results (2D projection)
# plt.figure(figsize=(8, 6))
# plt.scatter(gene_expression[:, 0], gene_expression[:, 1], c=cluster_labels, cmap='coolwarm', alpha=0.7)
# plt.title('Cell Clustering Based on Gene Expression', fontsize=14)
# plt.xlabel('Gene 1 Expression', fontsize=12)
# plt.ylabel('Gene 2 Expression', fontsize=12)
# plt.colorbar(label='Cluster')
# plt.tight_layout()
# plt.show()


