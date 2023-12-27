from dataclasses import dataclass
from math import inf
from itertools import combinations
from functools import lru_cache

@dataclass
class Node:
    name: str
    rate: int
    nodes: list[str]
    open: bool = False


def parse_data(filename):
    tree = {}
    with open(filename) as f:
        for line in f.read().splitlines():
            node, paths = line.split(';')
            node, rate = node.split('=')
            _, node, *_ = node.split()
            path, *paths = paths.split(', ')
            path = path.split()[-1]
            tree[node] = Node(node, int(rate), [path, *paths])

    return tree


def shortest_path(s, tree):
    dist = {u: {v: inf if v not in tree[u].nodes else 1 for v in tree} for u in tree}
    dist[s][s] = 0
    for u in tree:
        for v in tree:
            for k in tree:
                dist[v][k] = min(dist[v][k], dist[v][u] + dist[u][k])
    return dist


def solve(start, tree, dist, ts):
    found = {}
    @lru_cache
    def travel(s, t, v):
        print(v)
        if value := found.get(v):
            return value
        if t <= 0:
            return 0
        result = 0
        for n in tree:
            new_t = t - dist[s][n] - 1
            if n != s and new_t >= 0 and n not in v:
                flow = new_ts * tree[n].rate
                k = v + (n,)
                result = max(travel(n, new_t, k) + flow, result)
                found[k] = result

        return result

    a = 0
    for n in tree:
        new_ts = ts - dist[start][n] - 1
        if n != start and tree[n].rate and new_ts >= 0:
            flow = new_ts * tree[n].rate
            a = max(travel(n, new_ts, (n,)) + flow, a)

    return a


# def solve(start, tree, dist, ts):
#     queue = [(start, ts, 0, set())]
#     found = {}
#     while queue and (current := queue.pop(0)):
#         s, t, pressure, v = current
#         for n in tree:
#             new_t = t - dist[s][n] - 1
#             if (rate := tree[n].rate) and new_t >= 0 and n not in v:
#                 p = pressure + (new_t * rate)
#                 u = v | {n}
#                 queue.append((n, new_t, p, u))
#                 k = frozenset(u)
#                 found[k] = max(found.get(k, 0), p)

#     return found
#


if __name__ == '__main__':
    tree = parse_data('example.txt')
    dist = shortest_path('AA', tree)
    paths = solve('AA', tree, dist, 30)
    print(paths)
    result = max(paths.values())
    print(result)
    assert result == 1651
    tree = parse_data('input.txt')
    dist = shortest_path('AA', tree)
    paths = solve('AA', tree, dist, 30)
    result = max(paths.values())
    print(result)
    assert result == 1857
    paths = solve('AA', tree, dist, 26)
    result = max(
        paths[me] + paths[elephant]
        for me, elephant in combinations(paths, 2)
        if me.isdisjoint(elephant)
    )
    print(result)
    assert result == 2536
