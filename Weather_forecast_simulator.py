import random
import matplotlib.pyplot as plt

# Parameters
days = 30
trials = 1000

# Probabilities
P_sunny_to_sunny = 0.7
P_rainy_to_rainy = 0.5

sunny_counts = []        # Track sunny days in each trial
sunny_day30_counter = 0  # How many times the 30th day is sunny

# For each trial
for _ in range(trials):
    current_weather = "sunny" if random.random() < 0.5 else "rainy"  # Random start
    sunny_days = 0
    sunny_days_list = []  # List to track which days are sunny
    
    for day in range(1, days + 1):
        if current_weather == "sunny":
            sunny_days += 1
            sunny_days_list.append(day)  # Track the sunny day
            if random.random() < P_sunny_to_sunny:
                current_weather = "sunny"
            else:
                current_weather = "rainy"
        else:  # rainy
            if random.random() < P_rainy_to_rainy:
                current_weather = "rainy"
            else:
                current_weather = "sunny"
    
    # Track the sunny days for this trial
    sunny_counts.append(sunny_days)
    
    # If you want to print the sunny days in each trial:
    print(f"Sunny days in trial {_ + 1}: {sunny_days_list}")
    
    # Count how many times day 30 is sunny
    if sunny_days_list[-1] == 30:
        sunny_day30_counter += 1

# Probability that day 30 is sunny
prob_sunny_day30 = sunny_day30_counter / trials
print(f"Probability of sunny weather on day 30: {prob_sunny_day30:.3f}")

# Histogram of total sunny days across all simulations
plt.figure(figsize=(10,6))
plt.hist(sunny_counts, bins=range(min(sunny_counts), max(sunny_counts)+1), color='orange', edgecolor='black')
plt.title("Distribution of Sunny Days over 30 Days (1000 Trials)")
plt.xlabel("Number of Sunny Days in 30-Day Period")
plt.ylabel("Frequency")
plt.grid(True)
plt.axvline(sum(sunny_counts)/len(sunny_counts), color='red', linestyle='--', label='Mean Sunny Days')
plt.legend()
plt.show()
