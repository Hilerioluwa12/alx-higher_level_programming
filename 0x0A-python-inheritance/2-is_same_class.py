#!/usr/bin/python3
"""Function that returns true"""


def is_same_class(obj, a_class):
    """
    confirm if object is exactly an instance of the class

    Args:

        obj (object):
        a_class (object class):

    Returns: True / False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
