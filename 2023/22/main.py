from dataclasses import dataclass, field


@dataclass
class Brick:
    range: tuple[tuple[int, int, int], tuple[int, int, int]]
    parents: list['Brick'] = field(default_factory=list)
    children: list['Brick'] = field(default_factory=list)

    def __hash__(self):
        return hash(self.range)


def parse_data(filename):
    with open(filename) as f:
        bricks = []
        for line in f.read().splitlines():
            start, end = line.split('~')
            x1, y1, z1 = start.split(',')
            x2, y2, z2 = end.split(',')
            x1, y1, z1 = int(x1), int(y1), int(z1)
            x2, y2, z2 = int(x2), int(y2), int(z2)
            b = Brick(((x1, y1, z1), (x2, y2, z2)))

            bricks.append(b)
        return bricks


def blocks(brick):
    (xd, yd, zd), (xf, yf, zf) = brick
    if xd < xf:
        return [(x, yd, zd) for x in range(xd, xf+1)]
    if yd < yf:
        return [(xd, y, zd) for y in range(yd, yf+1)]
    if zd < zf:
        return [(xd, yd, z) for z in range(zd, zf+1)]
    return [(xd, yd, zd)]


def isvalid(brick, occupied):
    return all((x,y,z) not in occupied for (x,y,z) in blocks(brick))


def fall(bricks):
    bricks = sorted(bricks, key=lambda brick: brick.range[0][2])
    occupied = set()
    result = []
    for brick in bricks:
        (xd, yd, zd), (xf, yf, zf) = brick.range

        while isvalid(((xd, yd, zd-1), (xf, yf, zf-1)), occupied) and zd-1 >= 1:
            zd -= 1
            zf -= 1

        b = Brick(((xd, yd, zd), (xf, yf, zf)))
        result.append(b)

        for (x, y, z) in blocks(b.range):
            occupied.add((x, y, z))

    return result


def supports(brick1, brick2):
    for block in blocks(brick1.range):
        x, y, z = block
        if (x, y, z + 1) in blocks(brick2.range):
            return True

    return False


def get_parents_and_children(bricks):
    bricks = sorted(bricks, key=lambda brick: brick.range[0][2])
    N = len(bricks)
    parents = {i: [] for i in range(N)}
    children = {i: [] for i in range(N)}
    for i, brick1 in enumerate(bricks):
        for j, brick2 in enumerate(bricks):
            if brick2.range[0][2] > brick1.range[1][2] + 1:
                break

            if j > i and supports(brick1, brick2):
                parents[j].append(i)
                children[i].append(j)
                brick2.parents.append(brick1)
                brick1.children.append(brick2)

    return parents, children


def can_disintigrate(parents):
    N = len(parents)
    disintegrationgraph = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(N):
            if parents[j] == [i]:
                disintegrationgraph[i].append(j)

    return sum(disintegrationgraph[i] == [] for i in range(N))


def max_disintigrate(children, bricks):
    bricks = sorted(bricks, key=lambda brick: brick.range[0][2])
    N = len(bricks)
    total = 0
    for B in range(N):
        vis = {i for i in range(N) if bricks[i].range[0][2] == 1}
        pile = [i for i in range(N) if bricks[i].range[0][2] == 1 and i != B]

        while len(pile) > 0:
            b = pile.pop()
            if b != B:
                for v in children[b]:
                    if v not in vis:
                        pile.append(v)
                        vis.add(v)

        total += N - len(vis)

    return total

bricks = parse_data('example.txt')
bricks = fall(bricks)
parents, children = get_parents_and_children(bricks)
result = can_disintigrate(parents)
print(result)
assert result == 5
result = max_disintigrate(children, bricks)
print(result)
assert result == 7
bricks = parse_data('input.txt')
bricks = fall(bricks)
parents, children = get_parents_and_children(bricks)
result = can_disintigrate(parents)
print(result)
result = max_disintigrate(children, bricks)
print(result)
