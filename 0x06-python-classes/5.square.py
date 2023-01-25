#!/usr/bin/python3
class Square:

    def __init__(self, size = 0) -> None:
        self.__size = self.size(size)
        pass

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        try:
            if value != type(int):
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        self.__size = value
    

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("#" * self.__size)
