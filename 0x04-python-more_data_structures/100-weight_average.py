#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
      return 0

    sum = 0
    sumtup = 0
    avg = 0
    for tup in my_list:
        pt = tup[0] * tup[1]
        sumtup = tup[1] + sumtup
        sum  = pt + sum
    avg = sum/sumtup
    return avg
