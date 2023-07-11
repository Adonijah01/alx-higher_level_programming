#!/usr/bin/python3
"""
Containsread_file function
"""


def read_file(filename=""):
    """""read text file(UTF8) and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        """adonijah Kiplimo"""
