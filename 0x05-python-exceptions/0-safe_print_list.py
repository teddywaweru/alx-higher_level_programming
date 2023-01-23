#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for val in my_list[:x]:
        try:
            print(f"{val}\n")
        except IndexError:
            print("failed.")
                


