#!/usr/bin/python3
"""
function that write Object to text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to text file, using  JSON repsentation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
        """adonijah kiplimo"""
