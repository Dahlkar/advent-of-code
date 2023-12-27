#!/usr/bin/env python3
from dataclasses import dataclass
from itertools import cycle, count, starmap

class Rock:
    def __init__(self, name, ints, pos=0b0010000):
        self.name = name
        self.ints = ints
        self.len = len(ints)
        self.pos = pos

    def can_move(self, dir):
        op = {'>': 0b0000001, '<': 0b1000000}
        for i in self.ints:
            if i & op[dir]:
                return False

        return True

    def move(self, dir):
        match dir:
            case '>':
                return Rock(self.name, [i >> 1 for i in self.ints], self.pos >> 1)
            case '<':
                return Rock(self.name, [i << 1 for i in self.ints], self.pos << 1)

    def overlaps(self, pile):
        for i, layer in zip(self.ints, pile):
            if i & layer:
                return True

        return False

@dataclass
class Jet:
    i: int
    dir: str


ROCKS = (
    Rock(
        'MINUS',
        (0b0011110,)
    ),
    Rock(
        'PLUS',
        (0b0001000,
         0b0011100,
         0b0001000)
    ),
    Rock(
        'L',
        (0b0000100,
         0b0000100,
         0b0011100)
    ),
    Rock(
        'LINE',
        (0b0010000,
         0b0010000,
         0b0010000,
         0b0010000)
    ),
    Rock(
        'SQUARE',
        (0b0011000,
         0b0011000)
    ),
)


def solve(instructions, total=2022):
    rocks, jets = cycle(ROCKS), cycle(instructions)
    pile = [0] * 10000
    top = len(pile)
    states = {}
    for n in count():
        rock = next(rocks)
        for y in count(top - rock.len - 3):
            jet = next(jets)
            if rock.can_move(jet.dir):
                moved = rock.move(jet.dir)
                if not moved.overlaps(pile[y:]):
                    rock = moved

            if rock.overlaps(pile[y + 1:]) or rock.len + y >= len(pile):
                for i in range(rock.len):
                    pile[y + i] |= rock.ints[i]
                break

        top = min(top, y)
        height = len(pile) - top

        state = (jet.i, rock.name, rock.pos)
        if prev := states.get(state):
            rcycle = n - prev['rock']
            hcycle = height - prev['height']
            diff = total - n - 1
            more, remain = divmod(diff, rcycle)
            if remain == 0:
                return hcycle * more + height
        else:
            states[state] = {
                'height': height,
                'rock': n,
            }


if __name__ == '__main__':
    input = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    instructions = list(starmap(Jet, enumerate(input)))
    result = solve(instructions)
    print(result)
    assert result == 3068
    result = solve(instructions, 1000000000000)
    print(result)
    assert result == 1514285714288
    with open('input.txt') as f:
        instructions = list(starmap(Jet, enumerate(f.read().splitlines()[0])))
        result = solve(instructions)
        print(result)
        assert result == 3137
        result = solve(instructions, 1000000000000)
        print(result)
