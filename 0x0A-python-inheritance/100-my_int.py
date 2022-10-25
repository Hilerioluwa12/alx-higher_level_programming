#!/usr/bin/python3
"""Modules of class MyInt"""

class MyInt(int):
    """
    class Myint that inherits from int
    """
    def __eq__(self, other):
        """ function that define equals to"""
        return int(self) != int(other)

    def __ne__(self, other):
        """function that defines not equal to"""
        return int(self) == int(other)
