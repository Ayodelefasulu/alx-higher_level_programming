#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = chr(ord(c) - 32) if 'a' <= c <= 'z' else c
        print("{}".format(upper), end="")
    print()
