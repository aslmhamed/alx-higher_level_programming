#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mulByTwo = {}
    for key, value in a_dictionary:
        mulByTwo[key] = value * 2
    return mulByTwo
