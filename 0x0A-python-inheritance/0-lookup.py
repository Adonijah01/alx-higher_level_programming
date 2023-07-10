#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of strings representing the object's attributes and methods.
    """
    return dir(obj)

