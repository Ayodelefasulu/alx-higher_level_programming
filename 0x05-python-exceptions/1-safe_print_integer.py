#!/usr/bin/python3


def safe_print_integer(value):
        try:
            int_value = int(value)
            if int_value:
                print("{:d}".format(int_value))
                return True
        except ValueError:
            return False
