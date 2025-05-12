#!/usr/bin/python3
from string import ascii_lowercase
n = (','. join(letter for letter in ascii_lowercase if letter not in ('q', 'e')))

print(n)
