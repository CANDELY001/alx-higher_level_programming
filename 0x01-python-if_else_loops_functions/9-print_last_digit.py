#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        n = number % 10
    else:
        n = (number * -1) % 10
    print("{:d}".format(n), end='')
    return (n)