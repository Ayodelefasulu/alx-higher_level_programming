#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result = []
    for list in my_list:
        if list % 2 == 0:
            result.append(True)
        if list % 2 != 0:
            result.append(False)
    return result
