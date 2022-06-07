#!/usr/bin/python3

if __name__ == "__main__":
    """Adds all arguments."""
    import sys

    args = sys.argv
    arg_count = len(args)
    sums = 0
    if arg_count == 1:
        print(0)
    else:
        for i in range(1, len(args), 1):
            sums += int(args[i])
        print("{:d}".format(sums))
