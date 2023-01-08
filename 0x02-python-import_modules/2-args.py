#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv)
    print(f"{args - 1} arguments{'.' if args < 2 else ':'}")
    for idx, arg in enumerate(sys.argv):
        if idx == 0:
            continue
        print(f"{idx}: {arg}")
