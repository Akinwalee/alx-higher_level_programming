#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        up += '{}'.format(chr(ord(i) - 32) if ord(i) > 96 else i)
    print(up)

uppercase("best")
uppercase("Best School 98 Battery street")
