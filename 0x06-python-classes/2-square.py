#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This clas defines the Square'''
    def __init__(self, size=0):
        '''This methods creates a new instance of square'''
        if type(size) is int:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a integer")
