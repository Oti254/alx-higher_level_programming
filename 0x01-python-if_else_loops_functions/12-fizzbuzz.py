#!/usr/bin/python3
# Function that prints numbers from 1 to 100 separated by space
# If the number is a multiple of both 3 and 5 printing FizzBuzz
# If a multiple of 3 print Fizz
# If a multiple of 5 print Buzz
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{i} ", end="")
