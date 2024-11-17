#!/usr/bin/python3
# Function that retrieves an element from a list

def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    return (my_list[idx])
