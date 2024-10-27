#!/usr/bin/python3
# Prints all possible combinations of two digits

for i in range(0, 10):
    for j in range(0, 10):
        if i == j or i > j:
            continue
        if i == 8 and j == 9:
            continue
        print(f"{i}{j}, ", end="")

print('89')
