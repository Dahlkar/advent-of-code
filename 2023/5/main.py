class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __and__(self, other):
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        if end - start > 0:
            return Range(start, end)
        return Range(0, 0)


class Map:
    def __init__(self, name, map):
        self.name = name
        self.map = []
        for row in map:
            if row != '':
                dest, source, range = row.split()
                self.map.append((int(dest), int(source), int(range)))

    def get_dest(self, x):
        for dest, source, range in self.map:
            if source <= x < source + range:
                offset = x - source
                return dest + offset

        return x

    def get_range_dest(self, x, r):
        destinations = []
        remainder = r
        for dest, source, range in self.map:
            overlap = max(min((source + range), (x + r)) - max(source, x), 0)
            if overlap > 0:
                offset = max(x - source, 0)
                destinations.append((dest + offset, overlap))

            remainder -= overlap
            if remainder == 0:
                break

        if remainder > 0:
            destinations.append((x, remainder))

        return destinations

def parse_data(filename):
    with open(filename) as f:
        data = f.read().split('\n\n')
        seeds = data.pop(0)
        _, seeds = seeds.split(':')
        seeds = seeds.split()
        maps = []
        for item in data:
            name, *instructions = item.split('\n')
            maps.append(Map(name, instructions))

        return seeds, maps

def get_seed_location(seeds, maps):
    locations = []
    for seed in seeds:
        source = seed
        for map in maps:
            dest = map.get_dest(int(source))
            source = dest

        locations.append(dest)

    return min(locations)

def get_seeds_location(seeds, map):
    result = []
    for seed, range in seeds:
        source = [(seed, range)]
        for map in maps:
            destinations = []
            for x, r in source:
                destinations.extend(map.get_range_dest(x, r))
            source = destinations

        result.extend(s[0] for s in source)

    return min(result)


if __name__ == '__main__':
    seeds, maps = parse_data('example.txt')
    result = get_seed_location(seeds, maps)
    assert result == 35
    # seeds, maps = parse_data('input.txt')
    # result = get_seed_location(seeds, maps)
    seeds, maps = parse_data('example.txt')
    seeds = iter(seeds)
    l = []
    for s in seeds:
        l.append((int(s), int(next(seeds))))
    result = get_seeds_location(l, maps)
    print(result)
    assert result == 46
    seeds, maps = parse_data('input.txt')
    seeds = iter(seeds)
    l = []
    for s in seeds:
        l.append((int(s), int(next(seeds))))
    result = get_seeds_location(l, maps)
    print(result)
    assert result == 50855035
