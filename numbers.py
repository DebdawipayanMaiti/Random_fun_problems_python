import math
# 1. Strong Number Check
def strong_number_check(n):
    return n == sum(math.factorial(int(digit)) for digit in str(n))
# 2. Sum of First N Natural Numbers
def sum_of_first_n(n):
    return n * (n + 1) // 2
# 3. Even or Odd Check
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
# 4. Factors of a Number
def factors_of_number(n):
    return [i for i in range(1, n+1) if n % i == 0]
# 5. Counting Vowels and Consonants in a String
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels), sum(1 for char in s if char.isalpha() and char not in vowels)
# 6. Reverse a Number
def reverse_number(n):
    return int(str(n)[::-1])
# 7. Finding GCD of Two Numbers
def find_gcd(a, b):
    return math.gcd(a, b)
# 8. Finding LCM of Two Numbers
def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)
# 9. Sum of Prime Numbers in a Range
def sum_of_primes_in_range(n):
    return sum(x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)))
# 10. Sum of Squares of Digits of a Number
def sum_of_squares_of_digits(n):
    return sum(int(digit)**2 for digit in str(n))
# 11. Harshad Number (Niven Number) Check
def harshad_number_check(n):
    return n % sum(int(digit) for digit in str(n)) == 0
# 12. Armstrong Number Check
def armstrong_number_check(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))
# 13. Perfect Number Check
def perfect_number_check(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
# 14. Prime Numbers in a Range
def prime_numbers_in_range(n):
    return [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
# 15. Palindrome Number Check
def palindrome_number_check(n):
    return str(n) == str(n)[::-1]
# 16. Automorphic Number Check
def automorphic_number_check(n):
    return str(n**2).endswith(str(n))
# Test the functions with user input
def main():
    print("Enter a number:")
    n = int(input())

    print("1. Strong Number Check:", strong_number_check(n))
    print("2. Sum of First N Natural Numbers:", sum_of_first_n(n))
    print("3. Even or Odd Check:", even_or_odd(n))
    print("4. Factors of Number:", factors_of_number(n))
    print("5. Reverse Number:", reverse_number(n))
    print("10. Sum of Squares of Digits:", sum_of_squares_of_digits(n))
    print("11. Harshad Number Check:", harshad_number_check(n))
    print("12. Armstrong Number Check:", armstrong_number_check(n))
    print("13. Perfect Number Check:", perfect_number_check(n))
    print("15. Palindrome Number Check:", palindrome_number_check(n))
    print("16. Automorphic Number Check:", automorphic_number_check(n))

    print("Enter a second number for GCD/LCM operations:")
    m = int(input())
    print("7. GCD of Two Numbers:", find_gcd(n, m))
    print("8. LCM of Two Numbers:", find_lcm(n, m))

    print("Enter a string for vowel and consonant count:")
    s = input()
    vowels, consonants = count_vowels_consonants(s)
    print("5. Vowels:", vowels, "Consonants:", consonants)

    print("9. Sum of Prime Numbers in Range:", sum_of_primes_in_range(n))
    print("14. Prime Numbers in Range:", prime_numbers_in_range(n))

import math
import sympy

# Named Number Checkers (one-liners packed in definitions)
def is_harshad(n): return n % sum(map(int, str(n))) == 0
def is_armstrong(n): return n == sum(int(d)**len(str(n)) for d in str(n))
def is_palindrome(n): return str(n) == str(n)[::-1]
def is_perfect(n): return n == sum(i for i in range(1, n) if n % i == 0)
def is_automorphic(n): return str(n**2).endswith(str(n))
def is_kaprekar(n): return n == sum(map(int, filter(None, [str(n**2)[:len(str(n**2))-len(str(n))], str(n**2)[-len(str(n)):]])))
def is_duck(n): return '0' in str(n)[1:]
def is_buzz(n): return n % 7 == 0 or str(n).endswith('7')
def is_spy(n): return (lambda d: sum(d) == eval('*'.join(map(str, d))))(list(map(int, str(n))))
def is_smith(n): return not sympy.isprime(n) and sum(map(int, str(n))) == sum(map(int, ''.join(map(str, sympy.factorint(n).elements()))))
def is_emirp(n): return sympy.isprime(n) and sympy.isprime(int(str(n)[::-1])) and n != int(str(n)[::-1])
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1
def is_sad(n): return not is_happy(n)
def is_triangular(n): return ((8*n + 1)**0.5).is_integer()
def is_square(n): return (n**0.5).is_integer()
def is_cube(n): return round(n**(1/3))**3 == n
def is_fibonacci(n): return ((5*n**2 + 4)**0.5).is_integer() or ((5*n**2 - 4)**0.5).is_integer()
def is_mersenne(n): return (n+1 & n) == 0 and n > 0
def is_factorial(n): return any(math.factorial(i) == n for i in range(1, n+1))
def is_neon(n): return sum(map(int, str(n**2))) == n
def is_strong(n): return n == sum(math.factorial(int(d)) for d in str(n))
def is_prime(n): return sympy.isprime(n)
def is_composite(n): return n > 1 and not sympy.isprime(n)
def is_even(n): return n % 2 == 0
def is_odd(n): return n % 2 != 0

# Checker for all types
def check_named_numbers(n):
    checks = {
        "Harshad": is_harshad(n),
        "Armstrong": is_armstrong(n),
        "Palindrome": is_palindrome(n),
        "Perfect": is_perfect(n),
        "Automorphic": is_automorphic(n),
        "Kaprekar": is_kaprekar(n),
        "Duck": is_duck(n),
        "Buzz": is_buzz(n),
        "Spy": is_spy(n),
        "Smith": is_smith(n),
        "Emirp": is_emirp(n),
        "Happy": is_happy(n),
        "Sad": is_sad(n),
        "Triangular": is_triangular(n),
        "Square": is_square(n),
        "Cube": is_cube(n),
        "Fibonacci": is_fibonacci(n),
        "Mersenne": is_mersenne(n),
        "Factorial": is_factorial(n),
        "Neon": is_neon(n),
        "Strong": is_strong(n),
        "Prime": is_prime(n),
        "Composite": is_composite(n),
        "Even": is_even(n),
        "Odd": is_odd(n)
    }
    print(f"\nProperties of {n}:")
    for k, v in checks.items():
        if v:
            print(f" - {k} Number")

# Try it out
if __name__ == "__main__":
    number = int(input("Enter a number to check: "))
    check_named_numbers(number)

