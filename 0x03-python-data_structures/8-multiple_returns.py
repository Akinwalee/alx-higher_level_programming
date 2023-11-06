#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstchar = sentence[0]
    if length == 0:
        fistchar = None

    return (length, firstchar)
