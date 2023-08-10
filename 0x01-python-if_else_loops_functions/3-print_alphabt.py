#!/usr/bin/python3
for ch in range(97, 122 + 1):
    if chr(ch) != 'e' and chr(ch) != 'q':
        print("{:c}".format(ch), end='')
