#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of arguments."""
    import sys

    index = 1  # index counter
    av = sys.argv[1:]  # argument list
    ac = len(av)  # argument count
    str = [("arguments" if ac > 1 else "argument"),
           ":"] if ac > 0 else ["arguments", "."]

    print("{:d} {}".format(ac, "".join(str)))

    for arg in av:
        print("{}: {}".format(index, arg))
        index = index + 1
