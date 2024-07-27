#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a list of lists """


def pascal_triangle(n):
    """returns a list of lists of integers"""
    if (n <= 0):
        return ([])
    ang = [[1]]
    for u in range(n - 1):
        num = [1]
        for k in range(u):
            num.append(ang[-1][0 + k] + ang[-1][1 + k])
        num.append(1)
        ang.append(num)
    return (ang)
