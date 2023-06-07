#!/usr/bin/python3
for s in range(ord('a'), ord('z') + 1):
    if chr(s) != 'e' and chr(s) != 'q':
        print('{:c}'.format(s), end='')
