#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be a integer")
    def area(self):
        return self.__size ** 2
