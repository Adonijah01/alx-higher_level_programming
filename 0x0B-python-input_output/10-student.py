#!/usr/bin/python3
"""defines class student."""


class Student:
    """Reps  student."""

    def __init__(self, first_name, last_name, age):
        """Inits a new Student.
        Args:
            first_name (str): The first name of student.
            last_name (str): The last name of student.
            age (int): the age the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary rep of the Student.
        If attr is list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    """adonijah kiplimo"""
