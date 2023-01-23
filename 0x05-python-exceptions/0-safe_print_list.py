#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]))
            ret += 1
        except IndexError:
            break
    print("")
    return ret


