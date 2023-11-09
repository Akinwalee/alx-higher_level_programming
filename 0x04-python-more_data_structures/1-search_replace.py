#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [i for i in my_list if i is not search else replace]

    return (new_list)
