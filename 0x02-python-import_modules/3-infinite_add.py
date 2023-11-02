#!/usr/bin/python3
from sys import argv

add_argv = 0

for i in argv:
    add_argv += int(i)

print(add_argv)
