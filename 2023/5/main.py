class Range:
    def __init__(self, start, range):
        self.start = start
        self.end = start + range

    def __str__(self):
        return f'Range({self.start}, {self.end})'

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.end - self.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __and__(self, other):
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        range = end - start
        if range > 0:
            return Range(start, range)
        return Range(0, 0)

    def __sub__(self, other):
        diff = []
        if self.start < other.start:
            diff.append(Range(self.start, other.start - self.start))

        if self.end > other.end:
            diff.append(Range(other.end, self.end - other.end))

        return diff


class Map:
    def __init__(self, name, map):
        self.name = name
        self.map = []
        for row in map:
            if row != '':
                dest, source, range = (int(i) for i in row.split())
                dest_range = Range(dest, range)
                source_range = Range(source, range)
                self.map.append((source_range, dest_range))

    def get_range_dest(self, x):
        destinations = []
        for source, dest in self.map:
            overlap = source & x
            if overlap:
                offset = overlap.start - source.start
                destination = Range(dest.start + offset, len(overlap))
                destinations.append(destination)
                diff = x - source
                for i in diff:
                    destinations.extend(self.get_range_dest(i))

                return destinations

        return [x]


def parse_data(filename, range=False):
    with open(filename) as f:
        data = f.read().split('\n\n')
        seeds = data.pop(0)
        _, seeds = seeds.split(':')
        seeds = seeds.split()
        l = []
        if range:
            seeds = iter(seeds)
            for s in seeds:
                l.append(Range(int(s), int(next(seeds))))
            seeds = l
        else:
            for s in seeds:
                l.append(Range(int(s), 1))
            seeds = l

        maps = []
        for item in data:
            name, *instructions = item.split('\n')
            maps.append(Map(name, instructions))

        return seeds, maps


def get_seeds_location(seeds, maps):
    source = seeds
    for map in maps:
        destinations = []
        for range in source:
            destinations.extend(map.get_range_dest(range))
        source = destinations

    return min(s.start for s in source)


if __name__ == '__main__':
    seeds, maps = parse_data('example.txt')
    result = get_seeds_location(seeds, maps)
    print(result)
    assert result == 35
    seeds, maps = parse_data('input.txt')
    result = get_seeds_location(seeds, maps)
    print(result)
    assert result == 157211394
    seeds, maps = parse_data('example.txt', range=True)
    result = get_seeds_location(seeds, maps)
    print(result)
    assert result == 46
    seeds, maps = parse_data('input.txt', range=True)
    result = get_seeds_location(seeds, maps)
    print(result)
    assert result == 50855035
