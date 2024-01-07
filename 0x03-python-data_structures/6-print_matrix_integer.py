#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    row_num = len(matrix)

    for row in matrix:
        new_elements = len(row)
        col = 0

        for num in row:
            if col < new_elements - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end="")
            col += 1
        print()
