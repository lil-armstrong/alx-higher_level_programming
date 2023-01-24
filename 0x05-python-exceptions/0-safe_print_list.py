#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list."""
    nelem = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
        except Exception as exp:
            break
        else:
            nelem = nelem + 1
    print("")
    return nelem
