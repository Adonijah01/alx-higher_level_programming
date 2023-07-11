#!/usr/bin/python3
"""
contains the "class_to_json" function
"""


def class_to_json(obj):
    """return dictionary description with  data structure
    (list, dictionary, string, integer and boolean)
JSON serialization of object"""
    return obj.__dict__
"""adonijah kiplimo"""
