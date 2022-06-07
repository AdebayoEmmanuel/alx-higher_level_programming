#!/usr/bin/python3
def max_integer(my_list=[]):
    sorted_list = sorted(my_list, reverse = True)
    if len(my_list) == 0:
        return None
    return sorted_list[0]
    
