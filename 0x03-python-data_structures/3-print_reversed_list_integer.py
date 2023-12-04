#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # length = len(my_list) - 1
    for i in reversed(my_list):
        print('{:d}'.format(i))


'''def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
'''
