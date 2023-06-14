#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    ssum = 0
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for r in reversed(roman_string):
        digits = romans[r]
       ssum += digits if ssum < digits * 5 else -digits
    return ssum
