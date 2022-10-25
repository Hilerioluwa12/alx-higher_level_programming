#!/usr/bin/python3
"""Modules of class MyInt"""

class MyInt(int):
    """
    class Myint that inherits from int
    """
    def __eq__(self, other):
    """ function that define equals to"""
        if int(self) == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
    """function that defines not equal to"""
        if int(self) != int(other):
            return False
        else:
            return True
