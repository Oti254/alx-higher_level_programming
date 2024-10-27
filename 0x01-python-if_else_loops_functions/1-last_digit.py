#!/usr/bin/python3
# Prints the last digit of a random number
# Evaluates the range of the last digit

import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
print(f"The last digit of {number} is {last_digit} ", end="")
if last_digit > 5:
    print("and last digit is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
