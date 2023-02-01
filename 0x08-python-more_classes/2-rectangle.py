#!/usr/bin/python3
class Rectangle:
    def __init__(self, height=0, width=0) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width;

    @width.setter
    def width(self, value):
        if type(value) != 'int':
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            
        self.__width: int = value;

    @property
    def height(self):
        return self.__height;

    @height.setter
    def height(self, value):
        if type(value) != 'int':
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            
        self.__height: int = value;

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__width + self.__height ) * 2

        
