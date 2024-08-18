#!/usr/bin/python3
"""script that reads stdin line"""


import sys


total = 0
stat = {}
def print_code():
    print("File size", total)
    for c in sorted(stat.keys()):
        print(c, ":", stat[c])
try:
    for u, line in enumerate(sys.stdin):
        p = line.split()
        if len(p) != 10 or p[3] != 'GET' or p[4] != '/projects/260' or p[5] != 'HTTP/1.1':
            continue
        op = int(p[7])
        size = int(p[8])
        if op in stat:
            stat[op] += 1
        else:
            stat[op] = 1
        if (u + 1) % 10 == 0:
            print_code()
except KeyboardInterrupt:
    print_code()
