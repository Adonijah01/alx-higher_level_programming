#!/usr/bin/python3
"""
contains class "student"
"""


class Student:
    """Rep of student"""
    def __init__(self, first_name, last_name, age):
        """Inits the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return  dictionary reps of student instance"""
        return self.__dict__
    """adonijah kiplimo"""
