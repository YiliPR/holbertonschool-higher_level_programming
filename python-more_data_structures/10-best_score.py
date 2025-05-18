#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    num = 0

    for value in a_dictionary.values():
        if value > num:
            num = value
    
    for key, value in a_dictionary.items():
        if value == num:
            best_key = key
    
    return best_key
