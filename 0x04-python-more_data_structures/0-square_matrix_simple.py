#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        n_matrix = []
        for i in matrix:
            n_matrix.append(list(map(lambda x: x**2, i)))
        return (n_matrix)
