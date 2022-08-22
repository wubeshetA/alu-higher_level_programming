#!/usr/bin/python3
"""a script that multiply a matrix"""


def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for item in m_a:
        if len(item) != len(m_a[0]):
            raise ValueError("m_a must be a square matrix")
        if type(item) != list:
            raise TypeError("m_a must be a list of lists")
        for element in item:
            if type(element) != int and type(element) != float:
                raise TypeError("m_a should contain only integers or floats")

    for item in m_b:
        if len(item) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        if type(item) != list:
            raise TypeError("m_b must be a list of lists")
        for element in item:
            if type(element) != int and type(element) != float:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or all(len(item) == 0 for item in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(item) == 0 for item in m_b):
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
