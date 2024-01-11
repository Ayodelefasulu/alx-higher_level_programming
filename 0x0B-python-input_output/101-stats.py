#!/usr/bin/python3
"""This module prints statistics of metrics"""


import sys

def print_metrics(total_size, status_counts):
    """
    Print metrics based on total file size and status code counts.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts for each status code.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{:d}: {:d}".format(code, status_counts[code]))

def update_metrics(line, total_size, status_counts):
    """
    Update metrics based on the input line.

    Args:
        line (str): Input line in the specified format.
        total_size (int): Current total file size.
        status_counts (dict): Dictionary containing counts for each status code.

    Returns:
        int: Updated total file size.
        dict: Updated status code counts.
    """
    try:
        elements = line.split()
        size = int(elements[-1])
        code = int(elements[-2])

        total_size += size
        status_counts[code] = status_counts.get(code, 0) + 1

    except (ValueError, IndexError):
        pass

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_counts = update_metrics(line, total_size, status_counts)

            if i % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
