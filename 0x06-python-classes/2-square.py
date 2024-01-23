#!/usr/bin/python3

"""
Create A class named Square that defines a private instance attribute of: size.
"""


class Square:
    """
    defines class of square with optional size = zero
    initializing the variable self with size
    raise type and value errors if conditions not met
    """
    def __init__(self, size=0):
        #  Check it is type integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        #  Checks if size is less than zero
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
