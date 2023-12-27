from collections import defaultdict
import time
from math import inf

def parse_data(filename):
    with open(filename) as f:
        blueprints = []
        for line in f.read().splitlines():
            blueprint, instructions = line.split(': ')
            _, blueprint = blueprint.split()
            ins = {}
            for instruction in instructions.split('. '):
                type, costs = instruction.split(' costs ')
                _, type, *_ = type.split()
                c = []
                for cost in costs.split(' and '):
                    p, unit = cost.split()
                    unit = unit.replace('.', '')
                    c.append((int(p), unit))

                ins[type] = c
            blueprints.append({'id': int(blueprint), 'ins': ins})

    return blueprints


def use_blueprints(blueprints, time):
    quality = 0
    result = 1
    for blueprint in blueprints:
        geodes = use_blueprint(blueprint['ins'], time)
        quality += geodes * blueprint['id']
        result *= geodes

    return quality, result


def use_blueprint(blueprint, time):
    max_values = {}
    for costs in blueprint.values():
        for cost, material in costs:
            max_values[material] = max(max_values.get(material, 0), cost)
    queue = [(
        time,
        {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0},
        {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0},
        set(),
    )]
    best = 0
    while queue:
        t, resources, robots, v = queue.pop(0)
        if t <= 0:
            continue
        estimate = resources['geode'] + robots['geode'] * t
        if estimate > best:
            best = estimate

        if best - resources["geode"] >= (t * (2 * robots["geode"] + t - 1)) // 2:
            continue

        for robot, costs in blueprint.items():
            if robot in max_values and robots[robot] >= max_values[robot]:
                continue

            delta = max(
                0
                if (demand := cost - resources[material]) <= 0
                else inf
                if (supply := robots[material]) <= 0
                else (demand + supply - 1) // supply
                for cost, material in costs
            )
            if delta < t:
                new_robots = defaultdict(int, robots)
                new_robots[robot] += 1
                new_resources = defaultdict(int, resources)
                for r, n in robots.items():
                    new_resources[r] += n * (delta + 1)

                for cost, material in costs:
                    new_resources[material] -= cost

                new_t = t - delta - 1
                # n = tuple(new_robots.values()) + tuple(new_resources.values()) + (new_t,)
                # if n in v:
                #     continue
                u = v | {n}
                queue.insert(0, (new_t, new_resources, new_robots, u))

    return best


blueprints = parse_data('example.txt')
t = time.time()
result, _= use_blueprints(blueprints, 24)
print(time.time() - t)
print(result)
assert result == 33
# blueprints = parse_data('example.txt')
# t = time.time()
# _, result = use_blueprints(blueprints[:3], 32)
# print(time.time() - t)
# print(result)
# assert result == 62

blueprints = parse_data('input.txt')
t = time.time()
result, _ = use_blueprints(blueprints, 24)
print(time.time() - t)
print(result)
assert result == 2301
_, result = use_blueprints(blueprints[:3], 32)
print(time.time() - t)
print(result)
