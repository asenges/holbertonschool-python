#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    if len(argv) == 1:
        print(sum)
    if len(argv) > 1:
        for i in range(1, len(argv)):
            sum += int(argv[i], 10)
        print("{:d}".format(sum))
