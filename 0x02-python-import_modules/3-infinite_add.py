#!/usr/bin/python3

import sys
if __name__ == "__main__":
    sum_val = 0
    for arg in sys.argv[1:]:
        sum_val += int(arg)
    print(sum_val)
