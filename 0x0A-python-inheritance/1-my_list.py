#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """
    Mylist class

    Attributes:
        None
    """

    def __init__(self):
        """
        initializes list

        Arguments: None
        Returns: None
        """
        super().__init__

    def print_sorted(self):
        """
        prints sorted list
        Arguments: var

        Returns: None
        """
        var = []
        var = self.copy()
        var.sort()
        print(var)
