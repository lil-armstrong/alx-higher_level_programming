#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    av = sys.argv[1:]
    ac = len(av)

    if ac == 3:
        lh = int(av[0])
        opr = av[1]
        rh = int(av[2])
        res = 0

        ops = {'+': add, '-': sub, '*': mul, '/': div}
        if (opr in ops.keys()):
            print("{} {} {} = {}".format(lh, opr, rh, ops[opr](lh, rh)))
            exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
