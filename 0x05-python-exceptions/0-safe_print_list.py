#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a = 0
    for num in my_list:
        try:
            if my_list.index(num) == x:
                break
            else:
                numb = print(int(num), end="")
                a = a + 1
        except IndexError:
            print("This is not a number")
    print("\n")
    return a

"""def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
"""
