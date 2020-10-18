"""
    Recursive function to reverse a list.
"""


def reverse(l):
    if len(l) == 0:
        return []
    else:
        return [l.pop()] + reverse(l)
