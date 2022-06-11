#!/usr/bin/python3
for i in range(0, 100):
    left = i / 10
    right = i % 10
    if left < right and left != right and i !=89:
        print("{:02d}, ".format(i), end="")
    if i == 89:
        print("{:02d}".format(i), end="\n")
