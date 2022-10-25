#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class
    Attributes: None
    """

    def area(self):
        """Method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate integer value

        Returns: None
        """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
