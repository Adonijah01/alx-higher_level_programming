#!/usr/bin/python3
"""define function to scalar divide the matrix"""


def matrix_divided(matrix, div):
    """divide matrix by scalar integer, rounded by two decimal placs"""
    import decimal
    error_msg = "matrix must be  matrix of floats/integers"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of matrix must have same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be  number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix

"""adonijah kiplimo"""
