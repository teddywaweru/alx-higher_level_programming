#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div_list = []
    for val in my_list:
        div_list.append(True if val % 2 == 0 else False)

    return div_list
