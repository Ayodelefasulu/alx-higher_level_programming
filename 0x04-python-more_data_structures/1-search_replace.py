#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    nlist = []
    for list in new_list:
        if list == search:
            list = replace
        nlist.append(list)
    return nlist
