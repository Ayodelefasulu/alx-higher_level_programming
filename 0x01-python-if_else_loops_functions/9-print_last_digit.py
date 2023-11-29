#!/usr/bin/python3
def print_last_digit(number):
    numlast = abs(number) % 10
    print(numlast, end="")
    return numlast
