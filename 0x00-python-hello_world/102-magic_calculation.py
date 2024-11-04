#!/usr/bin/python3
import dis


def calculation(a, b):
    return 98 + (a ** b)


dis.dis(calculation)
