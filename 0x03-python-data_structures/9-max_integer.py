#!/usr/bin/python3
def max_integer(my_list=[]):
    lent = len(my_list)

    if lent == 0:
        return (None)

    max_num = my_list[0]

    for i in my_list:
        if i > max_num:
            max_num = i

    return (max_num)
