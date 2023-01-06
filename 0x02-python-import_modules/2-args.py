#!/usr/bin/python3
"""Print the number of arguments."""

if __name__ == "__main__":
    import sys

    index = 1  # index counter
    av = sys.argv[1:]  # argument list
    ac = 0  # argument count
    ac = len(av)
    str = [("arguments" if ac > 1 else "argument"),
           ":"] if ac > 0 else ["argument", "."]

    print("{} {}".format(ac, "".join(str)))

    for arg in av:
        print("{}: {}".format(index, arg))
        index = index + 1
