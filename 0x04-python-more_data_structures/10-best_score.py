#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)

    key1 = list(a_dictionary) [0]
    best = a_dictionary[key1]

    for key in a_dictionary.keys():
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    best_key = {i for i in a_dictionary if a_dictionary[i] == best}
    
    return (best_key)
