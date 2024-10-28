#!/usr/bin/python3
# Functon that converts a string to uppercase

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(i, end="")

    print()
