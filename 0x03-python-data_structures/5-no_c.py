#!/usr/bin/python3
def no_c(my_string):
    s_tran = {ord(i): None for i in 'cC'}
    new_str = my_string.translate(s_tran)
    return new_str
