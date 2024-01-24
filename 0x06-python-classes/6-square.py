#!/usr/bin/python3

"""
Create A class named Square
that defines a private instance attribute of: size, position.
And a public instance method def area(self):
that return the calculated area of the square
Method getters and setter properties for size
property def size(self): to retireve the size of the square
property setter def size(self, value): to set it:
Method getters and setters properties for position
property def position(self): to retrieve it
property setter def position(self, value): to set it
Public instance method: def my_print(self):
prints the square using #
and prints the position using spaces
"""


class Square:
    """
    defines class of square with optional size = zero
    initializing the variable self with size
    raise type and value errors if conditions not met
    """

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position
        Args:
            value (tuple): tuple of 2 positive integers
        Raises:
              TypeError: if value is not a tuple of two
                            positive integers

        """

        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns: the current square's area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints to the stdout the square with character #:
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
