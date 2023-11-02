#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)
names_ = []
for name in names:
    if name.startswith("__"):
        continue
    names_.append(name)
names_sorted = names_.sort()
for name in names_:
    print(name)


if __name__ == "__main__":
    pass

