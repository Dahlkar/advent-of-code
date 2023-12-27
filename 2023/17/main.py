#!/usr/bin/env python3
import heapq


def parse_data(filename):
    with open(filename) as f:
        return [line for line in f.read().splitlines()]


def shortest_path(s, e, grid, minsteps=1, maxsteps=3):
    queue = [(0, s, (0, 0))]
    seen = set()
    while queue:
        heat, u, d = heapq.heappop(queue)
        if u == e:
            return heat
        if (u, d) in seen:
            continue
        seen.add((u, d))
        x, y = u
        for dx, dy in {(0, 1), (0, -1), (1, 0), (-1, 0)} - {d, (-d[0], -d[1])}:
            a, b, h = x, y, heat
            for i in range(1, maxsteps + 1):
                a, b = a+dx, b+dy
                if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                    h += int(grid[b][a])
                    if i >= minsteps:
                        heapq.heappush(queue, (h, (a, b), (dx, dy)))


if __name__ == '__main__':
    grid = parse_data('example.txt')
    result = shortest_path((0, 0), (len(grid[0]) - 1, len(grid) - 1), grid)
    print(result)
    assert result == 102
    grid = parse_data('input.txt')
    result = shortest_path((0, 0), (len(grid[0]) - 1, len(grid) - 1), grid)
    print(result)
    assert result == 1244
    grid = parse_data('input.txt')
    result = shortest_path((0, 0), (len(grid[0]) - 1, len(grid) - 1), grid, 4, 10)
    print(result)
    assert result == 1367
