#!/usr/bin/python3
'''Defines a rectangle'''


class Rectangle:
    def __init__(self, width=0, height=0):
        '''Defines a rectangle width and height'''
        self.width = width
        self.height = height

    def __str__(self):
        '''creates a rectangle with #'''
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i != self.__height - 1:
                rect += '\n'
        return rect

    @property
    def width(self):
        '''getter for private width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for private width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for private height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for private height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''the perimeter of the rectangle'''
        return 2 * (self.__height + self.__width)
