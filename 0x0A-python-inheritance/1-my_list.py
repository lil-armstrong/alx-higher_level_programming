#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Represent my list"""

    def print_sorted(self):
        """Print sorted list (ascending sort)"""
        self.sort()
        print(self)
