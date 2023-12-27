#!/usr/bin/env python3
from dataclasses import dataclass
from itertools import count


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, o):
        ...


def parse_data(filename):
    rocks = set()
    start = ()
    grid = []
    graph = {}
    with open(filename) as f:
        for y, line in enumerate(f.read().split('\n')):
            row = []
            for x, c in enumerate(line):
                if c == 'S':
                    start = (x, y)
                if c == '#':
                    rocks.add((x, y))
                row.append(c)
                graph[(x, y)] = 1
            grid.append(row)

        return start, rocks, grid


def reached_garden_plots(start, rocks, grid, steps):
    positions = {start}
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_y = len(grid) - 1
    max_x = len(grid[0])
    for i in range(steps):
        new_positions = set()
        for x, y in positions:
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                x1, y1 = nx % max_x, ny % max_y
                if (x1, y1) not in rocks:
                    new_positions.add((nx, ny))

        positions = new_positions

    return len(positions)


def interpolate(f: list, xi: int) -> float:

    # Initialize result
    result = 0.0
    for i in range(len(f)):

        # Compute individual terms of above formula
        term = f[i][1]
        for j in range(len(f)):
            if j != i:
                term = term * (xi - f[j][0]) / (f[i][0] - f[j][0])

        # Add current term to result
        result += term

    return int(result)

start, rocks, grid = parse_data('input.txt')
w = len(grid[0])
r = w // 2
xs = [r, r + w, r + (w * 2)]
f = [(s, reached_garden_plots(start, rocks, grid, s)) for s in xs]
print(interpolate(f, 26501365))
start, rocks, grid = parse_data('example.txt')
f = [(s, reached_garden_plots(start, rocks, grid, s)) for s in xs]
result = interpolate(f, 5000)
print(result)
assert result == 16733044

# start, rocks, grid = parse_data('input.txt')
# result = reached_garden_plots(start, rocks, grid, 64)
# print(result)
# start, rocks, grid = parse_data('input.txt')
# result = reached_garden_plots(start, rocks, grid, 64)
# print(result)
