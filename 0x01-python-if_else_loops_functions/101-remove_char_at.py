#!/usr/bin/python3
def remove_char_at(str, n):
    char_mor = ''
    i = 0
    for c in str:
        if i != n:
            char_mor += str[i]
        i += 1
    return char_mor
