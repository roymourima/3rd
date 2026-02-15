# Calculate Factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
fact = factorial(number)
print(f"Factorial of {number} is: {fact}")



""" Write a Python program that:
   Asks the user for a number as input.
   Uses the math module to calculate the:
   Square root of the number
   Natural logarithm (log base e) of the number
   Sine of the number (in radians)
"""

import math

number = float(input("Enter a number: "))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

print("\nResults:")
print("Square root:", square_root)
print("Natural logarithm (base e):", natural_log)
print("Sine (in radians):", sine_value)