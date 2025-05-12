#!/usr/bin/python3
import sys

if __name__ == "__main__":

    length = len(sys.argv)


if length == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(length - 1))
    
    for arg in range(1, length):
        
        print("{}: {}".format(arg ,sys.argv[arg]))
