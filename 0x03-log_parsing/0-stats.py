#!/usr/bin/python3
"""script that reads stdin line"""


import sys


total = 0
stat = {}
num = 0
def print_code():
    print("File size: {}".format(total))
    for c in sorted(stat.keys()):
        print(f"{c}: {stat[c]}" )
try:
    for line in sys.stdin:
        p = line.strip()
        if len(p) != 10 or p[3] != 'GET' or p[4] != '/projects/260' or p[5] != 'HTTP/1.1':
            continue
        op = int(p[7])
        size = int(p[8])
        total += size
        if op in stat:
            stat[op] += 1
        else:
            stat[op] = 1
        num += 1
        if num % 10 == 0:
            print_code()
except KeyboardInterrupt:
    print_code()
