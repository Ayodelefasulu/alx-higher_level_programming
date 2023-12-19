#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        valueInt = int(value)
        print("{:d}".format(valueInt))
        return True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
