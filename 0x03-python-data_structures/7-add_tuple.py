#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    result1 = tuple_a[0] + tuple_b[0]
    result2 = tuple_a[1] + tuple_b[1]
    list_t = (result1, result2)
    return list_t
