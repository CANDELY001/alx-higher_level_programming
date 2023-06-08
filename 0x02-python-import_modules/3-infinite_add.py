#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    i = 0
    while i < len(sys.argv) - 1:
        sum += int(sys.argv[i + 1])
        i += 1
    print("{:d}".format(sum))
