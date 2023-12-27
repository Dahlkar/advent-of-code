from functools import reduce
import networkx as nx


def parse_data(filename):
    with open(filename) as f:
        edges = []
        for line in f.read().splitlines():
            key, nodes = line.split(':')
            for n in nodes.split():
                edges.append((key, n))

        return nx.from_edgelist(edges)


def part1(graph):
    min_edge_cut = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(min_edge_cut)
    return reduce(lambda x, y: x * y, [len(c) for c in nx.connected_components(graph)])


graph = parse_data('example.txt')
result = part1(graph)
print(result)
assert result == 54
graph = parse_data('input.txt')
result = part1(graph)
print(result)
