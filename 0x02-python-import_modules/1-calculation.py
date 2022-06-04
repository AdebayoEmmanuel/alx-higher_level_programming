#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)
    print(f"{a:d} + {b:d} = {add:d}".format(a, b, add))
    print(f"{a:d} - {b:d} = {sub:d}".format(a, b, sub))
    print(f"{a:d} * {b:d} = {mul:d}".format(a, b, mul))
    print(f"{a:d} / {b:d} = {div:d}".format(a, b, div))
