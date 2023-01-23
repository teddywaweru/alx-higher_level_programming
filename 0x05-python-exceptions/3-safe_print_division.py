#!/usr/bin/python3

def safe_print_division(a, b):
    div_val = None
    try:
        div_val = int(a) / int(b)
    
    except ZeroDivisionError:
        return div_val
    finally:
        print("{:d}".format(div_val))
    
