#!/usr/bin/python3

def element_at(my_list, idx):
    
    idx = my_list.index(idx)
    if (idx < 0) and (idx > my_list):
        print("None")
    else:
        return idx
