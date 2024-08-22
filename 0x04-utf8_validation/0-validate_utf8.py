#!/usr/bin/python3
"""data set represents a valid UTF-8 encoding"""
import utf8


def validUTF8(data):
    """data set represents a valid UTF-8 encoding"""
    try:
        utf8.decode(data)
        return (True)
    except utf8.DecoderError:
        return (False)
