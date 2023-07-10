#!/usr/bin/python3
"""
contains class MyInt
"""


class MyInt(int):
    """rebelver of integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """creates new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """whatwas != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """whatwas == is now !="""
        return int(self) == other
    """adonijah kiplimo"""
