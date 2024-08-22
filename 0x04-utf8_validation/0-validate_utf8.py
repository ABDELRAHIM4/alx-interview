#!/usr/bin/python3
"""data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """data set represents a valid UTF-8 encoding"""
    num = 0
    for byte in data:
        binary = bin(byte)[2:].zfill(8)
        if num == 0:
            if binary[0] == '0':
                continue
            if binary[:3] == '110':
                num = 1
            elif binary[:4] == '1110':
                num = 2
            elif binary[:5] == '11110':
                num = 3
            else:
                return (False)
        else:
            if binary[:2] == '10':
                return (False)
            num -= 1
    return (num == 0 )
