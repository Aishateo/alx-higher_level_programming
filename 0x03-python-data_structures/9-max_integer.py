#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)
    
    max_val = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > max_val:
            max_val = my_list[num]

    return (max_val)
