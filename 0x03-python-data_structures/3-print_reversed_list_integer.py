#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx = -1
    while idx > -len(my_list):
        print("{}\n".format(my_list[idx]))
        idx -= 1
