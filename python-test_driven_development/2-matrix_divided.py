#!/usr/bin/python3
"""Module that used to devide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix after dividing each element with div

    All elements of the matrix are divided by div, rounded by 2 decimal places

    Raises:
        TypeError: If elements of matrix are not integer or float.
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is zero.
        """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    first_row = matrix[0]
    for row in matrix:
        if len(row) != len(first_row):
            raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
