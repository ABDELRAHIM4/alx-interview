#!/usr/bin/python3
"""N queens puzzle is the challenge of placing N"""
import sys


def safe(n, row, col):
    """N queens puzzle is the challenge of placing N"""
    for i in range(row):
        if n[i] == col or\
            n[i] - 1 == col - row or \
            n[i] + 1 == col + row:
                return (False)
    return (True)


def solve(n, row, s):
    """N queens puzzle is the challenge of placing N"""
    if row == n:
        print([[i, col] for i, col in enumerate(s)])
        return
    for col in range(n):
        if safe(s ,row, col):
            s[row] = col
            solve(n, row + 1, s)

def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    solve(n, 0, [None] * n)

if __name__ == "__main__":
    main()
