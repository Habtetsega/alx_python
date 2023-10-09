#!/usr/bin/python3
import random

# This line should not be modified
number = random.randint(-10000, 10000)

# Extract the last digit of the number using modulus operator (%)
last_digit = abs(number) % 10

# Print the result based on the value of the last digit
print("The string Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
