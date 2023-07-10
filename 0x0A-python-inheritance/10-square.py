#!/usr/bin/python3
"""
Contains class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation ofsquare"""
    def __init__(self, size):
        """instantiation ofsquare"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return the area of square"""
        return self.__size ** 2
    """adonijah kiplimo"""
