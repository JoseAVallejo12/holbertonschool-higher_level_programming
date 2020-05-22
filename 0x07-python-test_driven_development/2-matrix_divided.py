#!/usr/bin/python3
# jose vallejo <1545@holbertonschool.com>
""" Create funtions for div matrix """


def matrix_divided(matrix, div):
    """ funtin for div each elemt of matrix """
    new_mtrx = []

    if not isinstance(div, (int, float)):
        """ div must be a number integer or float """
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (matrix):
        row_prev = len(matrix[0])
        for i in range(0, len(matrix)):
            new_mtrx.append([])
            if row_prev != len(matrix[i]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
            for j in range(0, len(matrix[i])):
                if not isinstance(matrix[i][j], (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
                else:
                    value = float(matrix[i][j] / div)
                    new_mtrx[i].append(round(value, 2))

            row_prev = len(matrix[i])
        return new_mtrx
