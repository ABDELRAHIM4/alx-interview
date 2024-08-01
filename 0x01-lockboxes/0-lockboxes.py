#!/usr/bin/python3
def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    arr = len(boxes)
    stored = set([0])
    keys = [0]
    while keys:
        key = keys.pop()
        for new in boxes[key]:
            if new not in stored and 0 <= new < arr:
                stored.add(new)
                keys.append(new)
    return (len(stored) == arr)
