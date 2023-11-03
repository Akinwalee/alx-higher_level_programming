#!/usr/bin/python3
def magic_calculation(a, b):
    add = lambda a, b: a + b
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
        return c
    else:
        sub = lambda a, b: a - b
        returnsub(a, b)
