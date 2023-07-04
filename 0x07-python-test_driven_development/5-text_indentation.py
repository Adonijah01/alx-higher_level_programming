#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation supplies function, text_indentation.
"""


def text_indentation(text):
    """splits text to lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")

                """adonijah Kiplimo"""
