#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute size.
"""

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a square.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
