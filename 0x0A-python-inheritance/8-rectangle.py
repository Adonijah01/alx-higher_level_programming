#!/usr/bin/python3
"""
Contain class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representation of Rectangle"""
    def __init__(self, width, height):
        """instant act of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        """adonijah kiplimo"""
