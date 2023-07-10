#!/usr/bin/python3
"""
contains the my_List clas
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initialises the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
        """adonijah Kiplimo"""
