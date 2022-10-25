#!/usr/bin/python3
"""Function that define a list of attribute"""


def lookup(obj):
    """ list of available attribute and methods of an object"""

    """
    Arguments:
        obj: object

    Returns: list
    """

    return dir(obj)
