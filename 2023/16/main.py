#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

def parse_data(filename):
    with open(filename) as f:
        return [line for line in f.read().splitlines()]


def energize(grid, start, d):
    queue = [(start, d, set())]
    visited = set()
    while queue:
        position, direction, path = queue.pop(0)
        x = position[0] + direction[0]
        y = position[1] + direction[1]
        next = (x, y)
        if (next, direction) in path or x < 0 or y < 0:
            continue

        try:
            g = grid[y][x]
        except IndexError:
            continue

        newdirection = direction
        if g == '|':
            if direction[0] != 0:
                queue.append((next, (0, -1), path))
                newdirection = (0, 1)
        if g == '-':
            if direction[1] != 0:
                queue.append((next, (-1, 0), path))
                newdirection = (1, 0)

        if g == '/':
            if direction[0] < 0:
                newdirection = (0, 1)
            if direction[0] > 0:
                newdirection = (0, -1)
            if direction[1] > 0:
                newdirection = (-1, 0)
            if direction[1] < 0:
                newdirection = (1, 0)

        if g == '\\':
            if direction[0] < 0:
                newdirection = (0, -1)
            if direction[0] > 0:
                newdirection = (0, 1)
            if direction[1] > 0:
                newdirection = (1, 0)
            if direction[1] < 0:
                newdirection = (-1, 0)

        path.add((next, direction))
        queue.append((next, newdirection, path))
        visited.add(next)

    return len(visited)


if __name__ == '__main__':
    grid = parse_data('example.txt')
    result = energize(grid, (-1, 0), (1, 0))
    print(result)
    assert result == 46
    result = max(*[energize(grid, (x, -1), (0, 1)) for x in range(len(grid[0]))],
                 *[energize(grid, (x, len(grid)), (0, -1)) for x in range(len(grid[0]))],
                 *[energize(grid, (-1, y), (1, 0)) for y in range(len(grid))],
                 *[energize(grid, (len(grid[0]), y), (-1, 0)) for y in range(len(grid))],
                 )
    print(result)
    assert result == 51
    grid = parse_data('input.txt')
    result = energize(grid, (-1, 0), (1, 0))
    print(result)
    assert result == 7307
    result = max(*[energize(grid, (x, -1), (0, 1)) for x in range(len(grid[0]))],
                 *[energize(grid, (x, len(grid)), (0, -1)) for x in range(len(grid[0]))],
                 *[energize(grid, (-1, y), (1, 0)) for y in range(len(grid))],
                 *[energize(grid, (len(grid[0]), y), (-1, 0)) for y in range(len(grid))],
                 )
    print(result)
    # for i, row in enumerate(grid):
    #     line = ''
    #     for j, c in enumerate(row):
    #         if (j, i) in result:
    #             c = '#'
    #         line += c

    #     print(line)
