#!/usr/bin/python3
# Checks if a random number is less than 0, equal to zero or greater than zero

import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
