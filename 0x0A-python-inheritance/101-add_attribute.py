#!/usr/bin/python3
"""Defines function thatadds attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to object if possible.
    Args:
        obj (any): object to add an attribut
        att (str): name of the attribute to add to object.
        value (any): value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
    """adonijah kiplimo"""
