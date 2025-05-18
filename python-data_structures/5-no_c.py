#!/usr/bin/python3

def no_c(my_string):
    letter = ""
    
    for char in my_string:
        if char.lower() != 'c':
            letter += char
            return letter
