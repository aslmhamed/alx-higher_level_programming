#!/usr/bin/python3

"""
Create A class named Square that defines a private instance attribute of: size.
And a public instance method def area(self):
that return the calculated area of the square
Method getters and setter properties for size
property def size(self): to retireve the size of the square
property setter def size(self, value): to set it:
"""


class Square:
    """
    defines class of square with optional size = zero
    initializing the variable self with size
    raise type and value errors if conditions not met
    """
    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        #  Check it is type integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        #  Checks if size is less than zero
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns: the current square's area
        """
        return self.__size ** 2
