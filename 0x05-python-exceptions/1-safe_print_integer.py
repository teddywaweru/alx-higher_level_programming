#!/usr/bin/python3

def safe_print_integer(value):
    val = False
    try:
        print("{:d}\n".format(value))
        val = True

    except (TypeError, ValueError):
        print("Error.")

    return val
