#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a, op, b = int(argv[1]), argv[2], int(argv[3])

if op == "+":
    print("{} + {} = {}".format(a, b, add(a, b)))
elif op == "-":
    print("{} - {} = {}".format(a, b, sub(a, b)))
elif op == "*":
    print("{} * {} = {}".format(a, b, mul(a, b)))
elif op == "/":
    print("{} / {} = {}".format(a, b, div(a, b)))
else:
    print("Uknown operator. Available operator: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    pass
