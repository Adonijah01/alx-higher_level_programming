#!/usr/bin/python3
"""
Contains inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj issubclass of a_class, otherwise return false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
"""adonijah Kiplimo"""
