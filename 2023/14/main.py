class RoundRock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self):
        self.rows = []
        self.rocks = []
        self.directions = [self.north, self.west, self.south, self.east]

    def add_row(self, row):
        self.rows.append(row)
        self.len = len(self.rows)
        self.width = len(row)

    def __len__(self):
        return self.len

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.rows))

    def __getitem__(self, i):
        return self.rows[i]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.rows])

    def add_rock(self, x, y):
        self.rocks.append(RoundRock(x, y))

    def cycle(self):
        for direction in self.directions:
            direction()

    def score(self):
        return sum(self.len - rock.y for rock in self.rocks)

    def north(self):
        self.rocks.sort(key=lambda i: i.y)
        for rock in self.rocks:
            while True:
                if rock.y > 0 and self[rock.y - 1][rock.x] == '.':
                    self[rock.y][rock.x] = '.'
                    rock.y -= 1
                    self[rock.y][rock.x] = 'O'
                else:
                    break

    def south(self):
        self.rocks.sort(key=lambda i: i.y, reverse=True)
        for rock in self.rocks:
            while True:
                if rock.y < self.len - 1 and self[rock.y + 1][rock.x] == '.':
                    self[rock.y][rock.x] = '.'
                    rock.y += 1
                    self[rock.y][rock.x] = 'O'
                else:
                    break

    def west(self):
        self.rocks.sort(key=lambda i: i.x)
        for rock in self.rocks:
            while True:
                if rock.x > 0 and self[rock.y][rock.x - 1] == '.':
                    self[rock.y][rock.x] = '.'
                    rock.x -= 1
                    self[rock.y][rock.x] = 'O'
                else:
                    break

    def east(self):
        self.rocks.sort(key=lambda i: i.x, reverse=True)
        for rock in self.rocks:
            while True:
                if rock.x < self.width - 1 and self[rock.y][rock.x + 1] == '.':
                    self[rock.y][rock.x] = '.'
                    rock.x += 1
                    self[rock.y][rock.x] = 'O'
                else:
                    break


def parse_data(filename):
    board = Board()
    with open(filename) as f:
        for y, line in enumerate(f.read().splitlines()):
            row = []
            for x, c in enumerate(line):
                if c == 'O':
                    board.add_rock(x, y)
                    
                row.append(c)

            board.add_row(row)

    return board


def part1(board):
    board.north()
    return board.score()


def part2(board):
    prev = {}
    for i in range(1_000_000_000):
        key = hash(board)
        if l := prev.get(key):
            loop = i - l
            a = (1_000_000_000 - i) % loop
            for n in range(a):
                board.cycle()

            return board.score()

        board.cycle()
        prev[key] = i

    return None


if __name__ == '__main__':
    board = parse_data('example.txt')
    result = part1(board)
    print(result)
    assert result == 136
    board = parse_data('input.txt')
    result = part1(board)
    print(result)
    assert result == 108955
    board = parse_data('example.txt')
    result = part2(board)
    print(result)
    assert result == 64
    board = parse_data('input.txt')
    result = part2(board)
    print(result)
    assert result == 106689
