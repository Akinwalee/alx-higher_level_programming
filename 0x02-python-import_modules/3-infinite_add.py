#!/usr/bin/python3
from sys import argv

add_argv = 0
argc = len(argv)

for i in range(argc):
    if i == 0:
        continue
    add_argv = add_argv + int(argv[i])

print(add_argv)

if __name__ == "__main__":
    pass
