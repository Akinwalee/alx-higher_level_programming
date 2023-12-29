#!/usr/bin/python3
"""Add items to Python list and save as JSON"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_list = []

for i in range(len(sys.argv)):
    if i == 0:
        continue
    my_list.append(i)

save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
