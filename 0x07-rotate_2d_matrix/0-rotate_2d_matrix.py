#!/usr/bin/python3
""" rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """ rotate it 90 degrees clockwise."""
    n = len(matrix)

    res = [[0] *  n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]
