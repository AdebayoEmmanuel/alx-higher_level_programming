#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv
    arg_count = len(args)
    count = 0
    if arg_count == 1:
        print("{:d} arguments.".format(count))
    elif arg_count == 2:
        count == 1
        print("{:d} argument:".format(count))
    else:
        for i in range(1, len(args), 1):
            count += 1
        print("{:d} arguments:".format(count))
    for i in range(1, len(args), 1):
        print("{}: {}".format(i, args[i]))
