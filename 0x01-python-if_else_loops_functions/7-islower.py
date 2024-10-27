#!/usr/bin/python3
# A function that checks for lowercase character

def islower(c):
    if (ord(c) > 96) and (ord(c) < 123):
        return True
    else:
        return False
