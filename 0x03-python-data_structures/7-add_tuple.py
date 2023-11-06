#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]
    
    res1 = a + c
    res2 = b + d

    return (res1, res2)
