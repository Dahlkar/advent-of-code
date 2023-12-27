from functools import reduce
from math import sqrt, ceil, floor


def parse_row(row):
    _, row = row.split(':')
    return [int(i) for i in row.split()]


def parse_file(filename):
    with open(filename) as f:
        times, distances, *_ = f.read().split('\n')
        times = parse_row(times)
        distances = parse_row(distances)

        return list(zip(times, distances))


def get_possible_solutions(data):
    result = []
    for t, d in data:
        possible = ceil((t + sqrt(t**2 - 4 * d))/2) - floor((t - sqrt(t**2 - 4 * d)) / 2) - 1
        result.append(possible)

    return reduce(lambda x, y: x * y, result)


def get_possible_solution(data):
    time = ''
    distance = ''
    for t, d in data:
        time += f'{t}'
        distance += f'{d}'

    t = int(time)
    d = int(distance)
    return ceil((t + sqrt(t**2 - 4 * d))/2) - floor((t - sqrt(t**2 - 4 * d)) / 2) - 1


if __name__ == '__main__':
    data = parse_file('example.txt')
    result = get_possible_solutions(data)
    print(result)
    assert result == 288
    data = parse_file('input.txt')
    result = get_possible_solutions(data)
    print(result)
    assert result == 625968
    data = parse_file('example.txt')
    result = get_possible_solution(data)
    print(result)
    assert result == 71503
    data = parse_file('input.txt')
    result = get_possible_solution(data)
    print(result)
    assert result == 43663323
