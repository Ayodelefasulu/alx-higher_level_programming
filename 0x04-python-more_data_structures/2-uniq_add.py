#!/usr/bin/python3


def uniq_add(my_list=[]):
    s = list(set(my_list))
    sum = 0
    i = 0
    while i < len(s):
        sum = s[i] + sum
        i = i + 1
    print(s)
    print(len(s))
    return sum
#    print(s)
