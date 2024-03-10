#!/usr/bin/python3
"""this script solves the pascal's triangle"""


def pascal_triangle(n):
    """this function returns a list of integers representing
    the pascal's triangle
    Args:
        n: number of rows to print
    """
    if n <= 0:
        return []
    triangle = [[1]]

    while len(triangle) != n:
        row = triangle[-1]
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
