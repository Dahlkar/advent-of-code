from functools import lru_cache
#/usr/bin/env python3
def parse_data(filename):
    with open(filename) as f:
        return [
            line.split() for line in f.read().splitlines()
        ]


def get_combinations(data):
    combinations = []
    s, numbers = data[0]
    numbers = [int(n) for n in numbers.split(',')]
    for s, numbers in data:
        numbers = tuple([int(n) for n in numbers.split(',')])
        combinations.append(match(s, numbers))

    return combinations

@lru_cache
def match(s, groups):
    count = 0
    if not groups:
        if '#' not in s:
            return 1
        return 0

    if len(s) < groups[0]:
        return 0

    if '.' not in s[:groups[0]]:
        if len(s) == groups[0] or s[groups[0]] != '#':
            count += match(s[groups[0] + 1:], groups[1:])

    if s[0] != '#':
        count += match(s[1:], groups)


    return count


def times_five(data):
    result = []
    for s, numbers in data:
        s = '?'.join([s] * 5)
        numbers = ','.join([numbers] * 5)
        result.append([s, numbers])

    return result

if __name__ == '__main__':
    data = parse_data('example.txt')
    result = get_combinations(data)
    print(sum(result))
    assert sum(result) == 21
    data = parse_data('input.txt')
    result = get_combinations(data)
    print(sum(result))
    assert sum(result) == 7402
    data = parse_data('example.txt')
    data = times_five(data)
    result = get_combinations(data)
    print(sum(result))
    assert sum(result) == 525152
    data = parse_data('input.txt')
    data = times_five(data)
    result = get_combinations(data)
    print(sum(result))
