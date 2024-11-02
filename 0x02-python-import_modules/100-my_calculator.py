#!/usr/bin/python3
# Program that imports functions from calculator_1.py

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    num = len(argv) - 1
    if num != 3:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in ["+", "-", "/", "*"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if operator == '+':
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {div(a, b)}")
