"""Simulate the blood pressure distribution of 1000 individuals based on two normal distributions: one for 
systolic pressure (mean = 120, std = 15) and one for diastolic pressure (mean = 80, std = 10). Normalize both 
distributions and classify the individuals into health risk categories based on systolic and diastolic pressure thresholds.
Steps:Generate 1000 random systolic and 1000 random diastolic blood pressure readings based on normal distributions.
Normalize both systolic and diastolic pressures to the range [0, 1].Classify individuals into categories based on systolic 
and diastolic thresholds:"""
# import numpy as np
# # Generate systolic and diastolic blood pressure samples
# systolic = np.random.normal(120, 15, 1000)
# diastolic = np.random.normal(80, 10, 1000)
# # Normalize both systolic and diastolic pressures to the range [0, 1]
# min_systolic, max_systolic = np.min(systolic), np.max(systolic)
# min_diastolic, max_diastolic = np.min(diastolic), np.max(diastolic)
# normalized_systolic = [(x - min_systolic) / (max_systolic - min_systolic) for x in systolic]
# normalized_diastolic = [(x - min_diastolic) / (max_diastolic - min_diastolic) for x in diastolic]
# # Classify based on thresholds
# risk_categories = {"Low Risk": 0, "Moderate Risk": 0, "High Risk": 0}
# for s, d in zip(normalized_systolic, normalized_diastolic):
#     if s < 0.3 and d < 0.3:
#         risk_categories["Low Risk"] += 1
#     elif s < 0.6 and d < 0.6:
#         risk_categories["Moderate Risk"] += 1
#     else:
#         risk_categories["High Risk"] += 1
# # Print risk category counts
# print(risk_categories)


"""Generate two random samples: one for male and one for female populations. Each sample will have different age 
distributions (e.g., male ages range from 18 to 65, and female ages range from 18 to 70). Normalize both samples 
to the range [0, 1], but use the weighted average of both normalized populations to classify into categories."""

# import numpy as np
# import matplotlib.pyplot as plt
# # Step 1: Generate random ages for males and females
# male_ages = np.random.randint(18, 66, 200)
# female_ages = np.random.randint(18, 71, 200)
# # Step 2: Normalize both age distributions to the range [0, 1]
# min_male = np.min(male_ages)
# max_male = np.max(male_ages)
# min_female = np.min(female_ages)
# max_female = np.max(female_ages)
# male_norm = [(x - min_male) / (max_male - min_male) for x in male_ages]
# female_norm = [(x - min_female) / (max_female - min_female) for x in female_ages]
# # Step 3: Weighted average of normalized male and female populations
# weighted_norm = [(0.6 * male + 0.4 * female) for male, female in zip(male_norm, female_norm)]
# # Step 4: Classify the weighted values into age groups
# age_groups = np.zeros(5)
# for norm in weighted_norm:
#     if norm < 0.2:
#         age_groups[0] += 1
#     elif norm < 0.4:
#         age_groups[1] += 1
#     elif norm < 0.6:
#         age_groups[2] += 1
#     elif norm < 0.8:
#         age_groups[3] += 1
#     else:
#         age_groups[4] += 1
# # Plotting the graphs
# fig, axs = plt.subplots(2, 2, figsize=(14, 10))
# # 1. Plot the male age distribution before normalization
# axs[0, 0].hist(male_ages, bins=20, color='blue', alpha=0.7, edgecolor='black')
# axs[0, 0].set_title('Male Age Distribution Before Normalization')
# axs[0, 0].set_xlabel('Age')
# axs[0, 0].set_ylabel('Frequency')
# # 2. Plot the female age distribution before normalization
# axs[0, 1].hist(female_ages, bins=20, color='green', alpha=0.7, edgecolor='black')
# axs[0, 1].set_title('Female Age Distribution Before Normalization')
# axs[0, 1].set_xlabel('Age')
# axs[0, 1].set_ylabel('Frequency')
# # 3. Plot the normalized male and female age distributions
# axs[1, 0].hist(male_norm, bins=20, color='blue', alpha=0.7, edgecolor='black', label='Male')
# axs[1, 0].hist(female_norm, bins=20, color='green', alpha=0.7, edgecolor='black', label='Female')
# axs[1, 0].set_title('Normalized Age Distributions (Male & Female)')
# axs[1, 0].set_xlabel('Normalized Age')
# axs[1, 0].set_ylabel('Frequency')
# axs[1, 0].legend()
# # 4. Plot the histogram of the weighted combined age distribution
# axs[1, 1].hist(weighted_norm, bins=20, color='purple', alpha=0.7, edgecolor='black')
# axs[1, 1].set_title('Weighted Combined Age Distribution')
# axs[1, 1].set_xlabel('Normalized Age')
# axs[1, 1].set_ylabel('Frequency')
# # Display all plots
# plt.tight_layout()
# plt.show()
# # Print the counts in the age groups
# print(f'Age Group Distribution: {age_groups}')

