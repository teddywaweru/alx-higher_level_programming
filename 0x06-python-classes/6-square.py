#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)) -> None:
        self.__size = self.size(size)
        self.__position = self.position(position)
    
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if value.length() != 2:
                raise TypeError
            for val in value:
                if val < 0:
                    raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")
                    
        self.__position = value
        
    
    def my_print(self):
        string = ""
        if self.__position[1] <= 0:
            string += "_" * self.__position[0]
        if self.__size != 0:
            string += "#" * self.__size
        print(string)
