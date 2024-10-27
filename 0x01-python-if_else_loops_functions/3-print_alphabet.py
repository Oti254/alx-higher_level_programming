#!/usr/bin/python3
# Prints the alphabet omitting q and e

for i in range(97, 123):
    if i == ord('q') or i == ord('e'):
        continue
    print(chr(i), end="")
