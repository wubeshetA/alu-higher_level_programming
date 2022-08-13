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
        for col in row:
            if isinstance(col, int) is not True and isinstance(col, float) is not True:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(matrix_divided(matrix, 3))
# print(matrix)
            