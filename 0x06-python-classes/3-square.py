#!/usr/bin/python3
class Square:

    def __init__(self, size = 0) -> None:
        self.__size = size
        try:
            if self.__size != type(int):
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        return self.__size ** 2

