#!/usr/bin/env python3
from math import lcm
from collections import defaultdict
from itertools import count


class Module:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        self.inputs = set()

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.connections})'

    @classmethod
    def create(cls, type, connections):
        if type[0] == '%':
            return FlipFlop(type.replace('%', ''), connections)

        if type[0] == '&':
            return Conjunction(type.replace('&', ''), connections)

        return Broadcaster(type, connections)

    def receive(self, pulse, origin):
        return (1, 0)

    def add_source(self, s):
        self.inputs.add(s)


class FlipFlop(Module):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.state = False

    def receive(self, pulse, origin):
        if self.state:
            self.state = False
            return (1, 0)
        self.state = True
        return (0, 1)

    def __hash__(self):
        return hash((self.name, self.state))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.connections}, {self.state})'


class Conjunction(Module):
    def __init__(self, name, connections):
        super().__init__(name, connections)
        self.state = {}

    def receive(self, pulse, origin):
        self.state[origin] = pulse
        if all(p == (0, 1) for p in self.state.values()):
            return (1, 0)
        return (0, 1)

    def add_source(self, s):
        super().add_source(s)
        self.state[s] = (1, 0)

    def __hash__(self):
        return hash((self.name, tuple(((k, v) for k, v in self.state.items()))))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.connections}, {self.state})'


class Broadcaster(Module):
    ...


def parse_data(filename):
    with open(filename) as f:
        g = {}
        for line in f.read().splitlines():
            type, connections = line.split(' -> ')
            module = Module.create(type, connections.split(', '))
            g[module.name] = module

        for s in g:
            for d in g[s].connections:
                if d in g:
                    g[d].add_source(s)

        return g


def simulate(g):
    pulses = [0, 0]
    for i in range(1000):
        queue = [('broadcaster', (1, 0), 'button', pulses)]
        while queue:
            m, pulse, origin, pulses = queue.pop(0)
            pulses[0] += pulse[0]
            pulses[1] += pulse[1]
            try:
                module = g[m]
            except KeyError:
                continue

            if isinstance(module, FlipFlop):
                if pulse == (0, 1):
                    continue

            pulse = module.receive(pulse, origin)
            for connection in module.connections:
                queue.append((connection, pulse, m, pulses))


    l , h = pulses
    return l * h


def simulate2(g):
    states = {}
    dest_node = next(n for n in g.values() if 'rx' in n.connections)
    for i in count(start=1):
        queue = [('broadcaster', (1, 0), 'button')]
        while queue:
            m, pulse, source = queue.pop(0)
            try:
                module = g[m]
            except KeyError:
                continue

            if pulse == (0, 1) and source in dest_node.inputs and source not in states:
                states[source] = i
                if set(states.keys()) == dest_node.inputs:
                    print(*(states.values()))
                    return lcm(*(states.values()))

            if isinstance(module, FlipFlop):
                if pulse == (0, 1):
                    continue

            pulse = module.receive(pulse, source)
            for connection in module.connections:
                queue.append((connection, pulse, m))


graph = parse_data('example1.txt')
result = simulate(graph)
print(result)
assert result == 32000000
graph = parse_data('example2.txt')
result = simulate(graph)
print(result)
assert result == 11687500
graph = parse_data('input.txt')
result = simulate(graph)
print(result)
graph = parse_data('input.txt')
result = simulate2(graph)
print(result)
