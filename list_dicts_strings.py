"""Given an array of integers, find all unique 
triplets whose sum is equal to a given target sum 
python
Copy
Edit
arr = [1, -2, 0, 5, -1, 2]  
s = 0  
Output: [(1, 4, 5), (0, 2, 4)]"""

# def find_triplets_with_sum(arr, s):
#     triplets = []
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if arr[i] + arr[j] + arr[k] == s:
#                     triplets.append((i, j, k))
#     return triplets

# # Example usage
# arr = [1, -2, 0, 5, -1, 2]
# s = 0
# print(find_triplets_with_sum(arr, s))  # Output: [(1, 4, 5), (0, 2, 4)]

"""Find All Unique Pairs Whose Product is 
Question: Given a list of numbers, find all 
unique pairs whose product is equal to a given number 
"""
# def find_pairs_with_product(arr, p):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] * arr[j] == p:
#                 pairs.append((i, j))
#     return pairs

# # Example usage
# arr = [2, 4, 1, 6, 5, 10]
# p = 20
# print(find_pairs_with_product(arr, p))  # Output: [(1, 5), (3, 4)]


"""Find the Closest Pair to a Target Sum
Question: Given a list of numbers and a target sums, 
find the pair whose sum is closest to 
�."""

# def find_closest_pair(arr, s):
#     closest_pair = None
#     closest_diff = float('inf')
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             diff = abs(arr[i] + arr[j] - s)
#             if diff < closest_diff:
#                 closest_diff = diff
#                 closest_pair = (arr[i], arr[j])
#     return closest_pair

# # Example usage
# arr = [10, 22, 28, 29, 30, 40]
# s = 54
# print(find_closest_pair(arr, s))  # Output: (22, 30)

"""Find Pairs with a Difference of 
Question: Given an array of integers, 
find all pairs where the absolute difference between 
numbers is 
"""

# def find_pairs_with_difference(arr, d):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if abs(arr[i] - arr[j]) == d:
#                 pairs.append((i, j))
#     return pairs

# # Example usage
# arr = [1, 5, 3, 4, 2]
# d = 2
# print(find_pairs_with_difference(arr, d))  # Output: [(0, 2), (2, 4), (1, 3)]


"""Find All Distinct Pairs with XOR Result Equal to 
Question: Given an array of integers, find all 
pairs where the bitwise XOR of two numbers is equal to 
."""


# def find_pairs_with_xor(arr, x):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] ^ arr[j] == x:
#                 pairs.append((i, j))
#     return pairs

# # Example usage
# arr = [5, 1, 2, 4, 3]
# x = 6
# print(find_pairs_with_xor(arr, x))  # Output: [(1, 2), (3, 4)]
""" Two-Sum with Hashing (Efficient Approach)
Question: Solve the original two-sum problem using a 
hash table for 
"""

# def find_pairs_with_sum_hashing(arr, s):
#     seen = {}
#     pairs = []
#     for i, num in enumerate(arr):
#         complement = s - num
#         if complement in seen:
#             pairs.append((seen[complement], i))
#         seen[num] = i
#     return pairs

# # Example usage
# arr = [2, 7, 11, 15]
# s = 9
# print(find_pairs_with_sum_hashing(arr, s))  # Output: [(0, 1)]


"""Find Pairs with Even/Odd Sum
Question: Find all pairs where the sum 
is even or odd."""

# def find_even_odd_sum_pairs(arr):
#     even_pairs = []
#     odd_pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if (arr[i] + arr[j]) % 2 == 0:
#                 even_pairs.append((i, j))
#             else:
#                 odd_pairs.append((i, j))
#     return even_pairs, odd_pairs

# # Example usage
# arr = [1, 2, 3, 4]
# even, odd = find_even_odd_sum_pairs(arr)
# print("Even Sum:", even)  # Output: [(1, 2), (2, 3)]
# print("Odd Sum:", odd)    # Output: [(0, 1), (0, 3), (1, 3)]


"""Find the Longest Consecutive Sequence:
Given an unsorted list of integers, find the longest 
subsequence where the elements are consecutive (step size of 1).
"""


# def find_longest_consecutive_sequence(arr):
#     arr = sorted(set(arr))  # Sort and remove duplicates
#     longest_seq = []
#     current_seq = []

#     for i in range(len(arr)):
#         if i == 0 or arr[i] == arr[i - 1] + 1:
#             current_seq.append(arr[i])
#         else:
#             if len(current_seq) > len(longest_seq):
#                 longest_seq = current_seq
#             current_seq = [arr[i]]

#     return max(longest_seq, current_seq, key=len)

# # Example usage
# arr = [1, 3, 5, 6, 7, 8, 10, 11]
# print(find_longest_consecutive_sequence(arr))  # Output: [5, 6, 7, 8]

"""Given a list of integers, return all consecutive 
subsequences.
"""

# def find_all_consecutive_sequences(arr):
#     arr = sorted(set(arr))  
#     sequences = []
#     current_seq = []

#     for i in range(len(arr)):
#         if i == 0 or arr[i] == arr[i - 1] + 1:
#             current_seq.append(arr[i])
#         else:
#             if len(current_seq) > 1:
#                 sequences.append(current_seq)
#             current_seq = [arr[i]]

#     if len(current_seq) > 1:
#         sequences.append(current_seq)

#     return sequences

# # Example usage
# arr = [1, 3, 5, 6, 7, 10, 11, 12]
# print(find_all_consecutive_sequences(arr))  # Output: [[5, 6, 7], [10, 11, 12]]

"""Given a sorted list of numbers, find the first 
missing number."""

# def find_first_missing_number(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] + 1 != arr[i + 1]:
#             return arr[i] + 1
#     return None  # No missing number

# # Example usage
# arr = [1, 2, 3, 5, 6, 8]
# print(find_first_missing_number(arr))  # Output: 4

"""Find the Longest Increasing Subsequence (Not Necessarily Consecutive)
Find the longest increasing subsequence where elements are in increasing order but not 
necessarily consecutive."""
# from bisect import bisect_left

# def longest_increasing_subsequence(arr):
#     sub = []
#     for num in arr:
#         pos = bisect_left(sub, num)
#         if pos == len(sub):
#             sub.append(num)
#         else:
#             sub[pos] = num
#     return sub

# # Example usage
# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# print(longest_increasing_subsequence(arr))  # Output: [10, 22, 33, 50, 60]


"""Find the Longest Arithmetic Progression in an Array
Find the longest subarray where the
 difference between adjacent elements is constant."""
 
 # def longest_arithmetic_progression(arr):
 #    if len(arr) < 2:
 #        return arr

#     longest_seq = []
#     current_seq = [arr[0]]
#     diff = None

#     for i in range(1, len(arr)):
#         if diff is None or arr[i] - arr[i - 1] == diff:
#             current_seq.append(arr[i])
#         else:
#             if len(current_seq) > len(longest_seq):
#                 longest_seq = current_seq
#             current_seq = [arr[i - 1], arr[i]]
#         diff = arr[i] - arr[i - 1]

#     return max(longest_seq, current_seq, key=len)

# # Example usage
# arr = [3, 6, 9, 12, 15, 20, 25, 30]
# print(longest_arithmetic_progression(arr))  # Output: [3, 6, 9, 12, 15]

 

"""Check if all elements of a list form a consecutive 
sequence (ignoring order)."""


# def is_consecutive_sequence(arr):
#     arr = sorted(arr)
#     return all(arr[i] + 1 == arr[i + 1] for i in range(len(arr) - 1))

# # Example usage
# arr = [3, 2, 4, 5, 6]
# print(is_consecutive_sequence(arr))  # Output: True
"""Count how many unique consecutive sequences exist in a list.
"""
# def count_consecutive_sequences(arr):
#     arr = sorted(set(arr))
#     count = 0
#     in_sequence = False

#     for i in range(len(arr) - 1):
#         if arr[i] + 1 == arr[i + 1]:
#             if not in_sequence:
#                 count += 1
#                 in_sequence = True
#         else:
#             in_sequence = False

#     return count

# # Example usage
# arr = [1, 2, 5, 6, 7, 10, 11, 15]
# print(count_consecutive_sequences(arr))  # Output: 3
