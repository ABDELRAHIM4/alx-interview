#!/usr/bin/python3
"""execute only two operations in this file"""


def minOperations(n: int) -> int:
    """execute only two operations in this file"""
    operat = 0
    cop = 2
    if n <= 1:
        return 0
    while n > 1:
        while n % cop == 0:
            operat += cop
            n //= cop
        cop += 1
    return operat
