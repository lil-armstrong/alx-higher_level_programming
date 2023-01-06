#!/usr/bin/python3


if __name__ == "__main__":
    """Print the result of the addition of all arguments."""
    import sys

    ac = sys.argv[1:]
    sum = 0
    for i in ac:
        if i.isnumeric() or int(i):
            sum += int(i)
    print("{:d}".format(sum))
