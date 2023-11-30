#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    result1 = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result1))

    result2 = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, result2))

    result3 = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, result3))

    result4 = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, result4))


if __name__ == "__main__":
    main()
