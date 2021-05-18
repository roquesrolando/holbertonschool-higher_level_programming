#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This class defines the attributes of a Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''This method creates a new instance of Square'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
    @property
    def position(self):
        '''Getter for position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for position'''
        try:
            self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''This method calculates the area of a square'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square'''
        size = self.__size
        x, y = self.__position

        if size == 0:
            print("")
        else:
            for i in range(y):
                print("")
            for j in range(size):
                for k in range(x):
                    print(" ", end="")
                for l in range(size):
                    print("#", end="")
                print("")
