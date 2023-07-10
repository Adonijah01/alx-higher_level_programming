#!/usr/bin/python3
"""
Contain class BaseGeometry
"""


class BaseGeometry:
    """ class with public instance methodarea and integer_validator"""
    def area(self):
        """raises exception whenit is  called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is an integer greater than0"""
        if type(value) is not int:
            raise TypeError("{:s} must be  integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        """adonijah kiplimo"""
