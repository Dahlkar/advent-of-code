from dataclasses import dataclass
from math import lcm


@dataclass
class Node:
    name: str
    left: str
    right: str

    def __hash__(self):
        return hash(self.name)

class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.start_nodes: set[Node] = set()

    def add_node(self, node: Node):
        self.nodes[node.name] = node
        if node.name[-1] == 'A':
            self.start_nodes.add(node)

    def __getitem__(self, name):
        return self.nodes[name]

    def __repr__(self):
        return str(self.nodes)


def create_graph(filename):
    with open(filename) as f:
        data = f.read()
        directions, map = data.split('\n\n')
        graph = Graph()
        for line in map.split('\n')[:-1]:
            name, paths = line.split(' = ')
            left, right = paths.replace('(', '').replace(')', '').split(', ')
            graph.add_node(Node(name, left, right))

        return directions, graph

def follow_directions(directions, graph):
    start = 'AAA'
    end = 'ZZZ'
    current = graph[start]
    i = 0
    while current.name != end:
        d = directions[i % len(directions)]
        match d:
            case 'L':
                current = graph[current.left]
            case 'R':
                current = graph[current.right]
            case _:
                raise Exception('invalid direction')

        i += 1
    return i


def follow_directions_two(start, directions, graph):
    current = start
    steps = 0
    while current.name[-1] != 'Z':
        d = directions[steps % len(directions)]
        match d:
            case 'L':
                current = graph[current.left]
            case 'R':
                current = graph[current.right]
            case _:
                raise Exception('invalid direction')

        steps += 1

    return steps

def find_steps(directions, graph):
    steps = []
    for start in graph.start_nodes:
        steps.append(follow_directions_two(start, directions, graph))

    return lcm(*steps)

if __name__ == '__main__':
    directions, graph = create_graph('example.txt')
    result = follow_directions(directions, graph)
    print(result)
    assert result == 2
    directions, graph = create_graph('example2.txt')
    result = follow_directions(directions, graph)
    print(result)
    assert result == 6
    directions, graph = create_graph('input.txt')
    result = follow_directions(directions, graph)
    print(result)
    assert result == 16897
    result = find_steps(directions, graph)
    print(result)
    directions, graph = create_graph('example3.txt')
    result = find_steps(directions, graph)
    print(result)
    assert result == 6
