#!/usr/bin/python3
"""Define Pascals Triangle func."""


def pascal_triangle(n):
    """Rep Pascal Triangle of size n.
    Return list of ints representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
"""adonijah kiplimo"""
