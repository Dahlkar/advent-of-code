#!/usr/bin/env python3
#
import sys
from collections import defaultdict
import random

DIRECTIONS = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}

def parse_data(filename):
    grid = []
    with open(filename) as f:
        for line in f.read().splitlines():
            row = []
            for c in line:
                row.append(c)

            grid.append(row)

    return grid

def find_neighbors(grid, start, terminals, slippery):
    neighbors = []
    q = [(start, 0, {start})]
    max_x = len(grid[0])
    max_y = len(grid)
    while q:
        p, l, seen = q.pop(0)
        if p in terminals and p != start:
            neighbors.append((p, l))
            continue

        adj = []
        x, y = p
        if (c := grid[y][x]) in DIRECTIONS and slippery:
            dx, dy = DIRECTIONS[c]
            nx, ny = x + dx, y + dy
            n = nx, ny
            if n not in seen:
                q.append((n, l + 1, seen | {n}))
                adj.append(n)

        else:
            for dx, dy in DIRECTIONS.values():
                nx, ny = x + dx, y + dy
                n = nx, ny
                if 0 <= nx < max_x and 0 <= ny < max_y and grid[ny][nx] != '#' and n not in seen:
                    adj.append(n)

        if len(adj) > 1 and p != start:
            neighbors.append((p, l))
            continue

        for n in adj:
            q.append((n, l + 1, seen | {n}))

    return neighbors


def build_dag(grid, start, end, slippery=True):
    queue = [start]
    dag = defaultdict(list)
    vis = set()
    while queue:
        point = queue.pop(0)

        if point in vis:
            continue

        vis.add(point)
        x, y = point

        for n, l in find_neighbors(grid, point, [start, end], slippery):
            dag[point].append((n, l))
            if n not in vis:
                queue.append(n)

    return dag

def longest_path(graph, start, end):
    longest, q = 0, [(start, 0, {start})]
    while q:
        p, l, seen = q.pop()
        if p == end:
            longest = max(longest, l)
            continue
        for n,nl in graph[p]:
            if n not in seen:
                q.append((n, l+nl, seen | {n}))
    return longest


sys.setrecursionlimit(10000)
data = parse_data('example.txt')
start, end = (1, 0), (len(data[0]) - 2, len(data) - 1)
dag = build_dag(data, start, end)
result = longest_path(dag, (1, 0), (len(data[0]) - 2, len(data) - 1))
print(result)
assert result == 94
dag = build_dag(data, (1, 0), (len(data[0]) - 2, len(data) - 1), slippery=False)
# dag = contract_dag(dag, (1, 0))
result = longest_path(dag, (1, 0), (len(data[0]) - 2, len(data) - 1))
print(result)
assert result == 154
data = parse_data('input.txt')
# dag = build_dag(data, (1, 0))
# result = longestPath(dag, (1, 0), (len(data[0]) - 2, len(data) - 1))
# print(result)
dag = build_dag(data, (1, 0), (len(data[0]) - 2, len(data) - 1), slippery=False)
print('built dag')
result = longest_path(dag, (1, 0), (len(data[0]) - 2, len(data) - 1))
print(result)
