#!/usr/bin/env python3

def parse(instructions):
    floor = 0
    position = 0
    for i, c in enumerate(instructions, start=1):
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1

        if position == 0 and floor == -1:
            position = i

    return floor, position

if __name__ == '__main__':
    with open('input.txt') as f:
        print(parse(f.read()))
