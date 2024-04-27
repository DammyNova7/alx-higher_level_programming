#!/usr/bin/python3

"""
An empty class
"""


class Square:

    """
    Simple class
    """
    def __init__(self, size=0):
        """
        Instantiation of the square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
