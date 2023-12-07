#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    else:
        if roman_string == 'I':
            return 1
