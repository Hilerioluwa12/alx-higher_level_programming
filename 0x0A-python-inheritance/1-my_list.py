#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """
    Mylist class

    Attributes:
        None
    """

    def print_sorted(self):
        """
        prints sorted list
        Arguments: var

        Returns: None
        """
        print(sorted(self))
