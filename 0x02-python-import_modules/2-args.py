#!/usr/bin/python3
# Program that prints the number of and list of its arguments

if __name__ == "__main__":
    from sys import argv

    num = len(argv)
    if num == 2:
        print(f"{num - 1} argument.")
    elif num == 1:
        print(f"{num - 1} arguments.")
    else:
        print(f"{num - 1} arguments:")
    for i in range(1, num):
        print(f"{i}: {argv[i]}")
