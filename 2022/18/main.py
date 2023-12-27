from itertools import starmap
from dataclasses import dataclass, field


@dataclass
class Cube:
    x: int
    y: int
    z: int
    sides: set[tuple[int, int, int]] = field(default_factory=set)

    def __post_init__(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)
        self.sides = {
            (self.x, self.y, self.z + 1): False,
            (self.x, self.y, self.z - 1): False,
            (self.x, self.y + 1, self.z): False,
            (self.x, self.y - 1, self.z): False,
            (self.x + 1, self.y, self.z): False,
            (self.x - 1, self.y, self.z): False,
        }


def get_surface_area(cubes):
    grid = {}
    for cube in cubes:
        grid[(cube.x, cube.y, cube.z)] = cube

    for cube in cubes:
        for point in cube.sides:
            n = grid.get(point)
            if isinstance(n, Cube):
                cube.sides[point] = True

    return sum(len(list(filter(lambda x: not x, cube.sides.values()))) for cube in cubes)


def get_contained(cubes):
    grid = {}
    for cube in cubes:
        grid[(cube.x, cube.y, cube.z)] = cube

    max_point = tuple(max(c[i] + 1 for c in grid) for i in range(3))
    min_point = tuple(min(c[i] - 1 for c in grid) for i in range(3))

    def in_space(n):
        return all(min_point[i] <= n[i] <= max_point[i] for i in range(3))

    queue = [max_point]
    exposed = 0
    visited = set()
    while queue:
        cube = queue.pop(0)
        if cube in grid:
            exposed += 1
            continue

        if cube not in visited:
            visited.add(cube)
            c = Cube(*cube)
            for n in c.sides:
                if in_space(n):
                    queue.append(n)

    return exposed


with open('example.txt') as f:
    cubes = list(starmap(Cube, (line.split(',') for line in f.read().splitlines())))
    result = get_surface_area(cubes)
    print(result)
    assert result == 64
    result = get_contained(cubes)
    print(result)
    assert result == 58


with open('input.txt') as f:
    cubes = list(starmap(Cube, (line.split(',') for line in f.read().splitlines())))
    result = get_surface_area(cubes)
    print(result)
    result = get_contained(cubes)
    print(result)
