#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
# turn number to string 
number = str(number)
# get the last digit of number and store in a var
lastDigit = number[-1]
# convert last digit back to int
lastDigit = int(lastDigit)
# check if number is -ve, multiply last digit by -1 if true
if number[0] == "-":
    lastDigit *= -1
# convert number back to int
number = int(number)
# check if last digit is 0, print the message
if lastDigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number,lastDigit))
# check if greater than 5, print the message
if lastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,lastDigit))
# check if less than 6, print the message
if lastDigit < 6 and lastDigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number,lastDigit))
