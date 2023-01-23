#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for val in my_list[:x]:
        try:
            print("{:d}".format(val))
        except:
            continue
    print("\n")
