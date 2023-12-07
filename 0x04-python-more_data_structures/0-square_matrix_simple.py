#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # m00 = matrix[0][0] * matrix[0][0]
    # m01 = matrix[0][1] * matrix[0][1]
    # m02 = matrix[0][2] * matrix[0][2]
    # m10 = matrix[1][0] * matrix[1][0]
    # m11 = matrix[1][1] * matrix[1][1]
    # m12 = matrix[1][2] * matrix[1][2]
    # m20 = matrix[2][0] * matrix[2][0]
    # m21 = matrix[2][1] * matrix[2][1]
    # m22 = matrix[2][2] * matrix[2][2]
    # new_matrix = [[m00, m01, m02], [m10, m11, m12], [m20, m21, m22]]
    new_matrix = []
    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
    #    return new_matrix
