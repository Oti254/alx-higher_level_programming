#!/usr/bin/python3
# Program that imports the function def add(a + b) from 0-add.py
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")
