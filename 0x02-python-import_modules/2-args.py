#!/usr/bin/python3
from sys import argv

argc = len(argv)

if argc == 1:
    print("0 arguments.")
else:
    print("{} argument{}:".format(argc - 1, "" if argc == 2 else "s"))
    for i in range(0, argc):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    pass
