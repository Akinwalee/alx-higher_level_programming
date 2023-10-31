#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for i, char in enumerate(str):
        if i == n:
            continue
        copy += "{}".format(char)
    return copy
