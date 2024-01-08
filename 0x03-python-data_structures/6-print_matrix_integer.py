#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    num_row = len(matrix)

    for row in matrix:
        num_elements = len(row)
        col = 0  # This will keep track of the column index

        for num in row:
            if col < num_elements - 1:
                print("{:d}".format(num)), end=" ")
            else:
                print("{:d}".format(num), end="")
            col += 1  # increment column index
        print()

