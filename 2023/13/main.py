#!/usr/bin/env python3
#
def parse_data(filename):
    with open(filename) as f:
        mirrors = f.read().split('\n\n')
        return [[line for line in mirror.splitlines()] for mirror in mirrors]


def find_reflections(mirrors, t_mirrors, errors=0):
    return [
        (find_reflection(mirror, errors) * 100) + find_reflection(t_mirror, 1)
        for mirror, t_mirror in zip(mirrors, t_mirrors)
    ]


def find_reflection(mirror, allowed=0):
    num_rows = len(mirror)
    num_col = len(mirror[0])
    for x in range(num_rows - 1):
        errors = 0
        for y in range(num_rows):
            left = x - y
            right = x + y + 1
            if 0 <= left < right < num_rows:
                for i in range(num_col):
                     if mirror[left][i] != mirror[right][i]:
                         errors += 1
        if errors == allowed:
            return x + 1

    return 0

def transpose_mirrors(mirrors):
    return [[list(l) for l in zip(*mirror)] for mirror in mirrors]


if __name__ == '__main__':
    mirrors = parse_data('example.txt')
    t_mirrors = transpose_mirrors(mirrors)
    reflections = find_reflections(mirrors, t_mirrors)
    print(sum(reflections))
    reflections = find_reflections(mirrors, t_mirrors, 1)
    print(sum(reflections))
    mirrors = parse_data('input.txt')
    t_mirrors = transpose_mirrors(mirrors)
    reflections = find_reflections(mirrors, t_mirrors)
    print(sum(reflections))
    reflections = find_reflections(mirrors, t_mirrors, 1)
    print(sum(reflections))
