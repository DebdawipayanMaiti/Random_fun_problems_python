# import random
# import matplotlib.pyplot as plt
# def simulate_monty_hall(trials=1000):
#     stay_wins, switch_wins = 0, 0
#     for _ in range(trials):
#         car = random.randint(0, 2)
#         choice = random.randint(0, 2)
#         host_options = [door for door in range(3) if door != choice and door != car]
#         host = random.choice(host_options)
#         switch = [door for door in range(3) if door != choice and door != host][0]
#         if choice == car:
#             stay_wins += 1
#         if switch == car:
#             switch_wins += 1
#     return stay_wins / trials, switch_wins / trials
# stay, switch = simulate_monty_hall()
# plt.bar(['Stay', 'Switch'], [stay, switch], color=['red', 'green'])
# plt.ylabel('Win Rate')
# plt.title('Monty Hall Simulation')
# plt.ylim(0, 1)
# plt.show()



# import random
# import matplotlib.pyplot as plt
# # Function to simulate a single round of the Monty Hall game
# def monty_hall(switch: bool):
#     # Randomly place the car behind one of the doors (0, 1, or 2)
#     car_position = random.randint(0, 2)
    
#     # The contestant randomly picks one of the doors (0, 1, or 2)
#     contestant_choice = random.randint(0, 2)
    
#     # Host opens a door that doesn't have the car and isn't the contestant's choice
#     # First, list the available doors
#     available_doors = [0, 1, 2]
#     available_doors.remove(contestant_choice)
#     if car_position in available_doors:
#         available_doors.remove(car_position)
#     # Host opens one of the remaining doors that doesn't have the car
#     host_opens = random.choice(available_doors)
    
#     # If contestant switches, they choose the remaining unopened door
#     if switch:
#         # The remaining door after removing the contestant's initial choice and the host's door
#         remaining_door = [0, 1, 2]
#         remaining_door.remove(contestant_choice)
#         remaining_door.remove(host_opens)
#         contestant_choice = remaining_door[0]
    
#     # Return True if the contestant wins (i.e., they chose the door with the car)
#     return contestant_choice == car_position
# # Function to simulate multiple rounds of the Monty Hall problem
# def simulate_monty_hall(num_rounds=1000):
#     stay_wins = 0
#     switch_wins = 0
#     for _ in range(num_rounds):
#         if monty_hall(switch=False):
#             stay_wins += 1
#         if monty_hall(switch=True):
#             switch_wins += 1
#     return stay_wins, switch_wins
# # Simulate the game and get the results
# num_rounds = 1000
# stay_wins, switch_wins = simulate_monty_hall(num_rounds)
# # Calculate win rates
# stay_win_rate = stay_wins / num_rounds
# switch_win_rate = switch_wins / num_rounds
# # Plot the results
# labels = ['Stay', 'Switch']
# win_rates = [stay_win_rate, switch_win_rate]
# plt.bar(labels, win_rates, color=['blue', 'green'])
# plt.title('Monty Hall Problem: Win Rates for Stay vs Switch')
# plt.ylabel('Win Rate')
# plt.ylim(0, 1)
# plt.show()
# # Output the results
# print(f"Stay Win Rate: {stay_win_rate:.4f}")
# print(f"Switch Win Rate: {switch_win_rate:.4f}")
