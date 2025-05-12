#!/usr/bin/python3
import sys
if __name__ == "__main__":

    total = 0
    for idx in range(1, len(sys.argv)):
        total += int(sys.argv[idx])
    print(total)

#["./3-infinite_add.py", "1", "2", "3", "4", "5"] = sys.argv
