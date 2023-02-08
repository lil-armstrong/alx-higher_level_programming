#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Represent my list"""

    def __init__(self):
        """initialize the instance."""
        super().__init__()

    def print_sorted(self):
        """Print sorted list (ascending sort)"""
        print(sorted(self))
