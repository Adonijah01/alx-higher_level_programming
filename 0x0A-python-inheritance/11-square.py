#!/usr/bin/python3
"""
ontains class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """ class with public instance method area and integer_validator"""
    def area(self):
        """raises exception whencalled"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that value isinteger greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of rectangle"""
    def __init__(self, width, height):
        """instants the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of  rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A representation of square"""
    def __init__(self, size):
        """instantiation of  square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    """adonijah Kiplimo"""
