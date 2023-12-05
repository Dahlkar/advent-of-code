import itertools
from functools import reduce


class Dot:
    ...


class Symbol:
    def __init__(self, symbol, x, y):
        self.symbol: str = symbol
        self.x: int = x
        self.y: int = y
        self.numbers: set[int] = set()

    def add_number(self, number):
        self.numbers.add(int(number))

    def gear_ratio(self):
        return reduce(lambda x, y: x * y, self.numbers)

    def __str__(self):
        return f'{self.symbol}: {self.numbers}'

    def __repr__(self):
        return str(self)


class PartsNumber:
    def __init__(self):
        self.number = ''


def parse_board():
    board = []
    symbols = []
    with open('input.txt') as f:
        y = 0
        for line in f.readlines():
            row = []
            x = 0
            num = PartsNumber()
            for s in line.replace('\n', ''):
                if s.isdigit():
                    num.number += s
                    row.append(num)
                elif s != '.':
                    symbol = Symbol(s, x, y)
                    symbols.append(symbol)
                    row.append(symbol)
                    num = PartsNumber()
                else:
                    row.append(Dot())
                    num = PartsNumber()
                x += 1

            board.append(row)
            y += 1

    return board, symbols


def find_numbers(board, symbols):
    max_y = len(board)
    max_x = len(board[0])

    x_directions = (lambda x: x, lambda x: max(x-1, 0), lambda x: min(x+1, max_x))
    y_directions = (lambda y: y, lambda y: max(y-1, 0), lambda y: min(y+1, max_y))
    directions = list(itertools.product(x_directions, y_directions))
    for symbol in symbols:
        for fx, fy in directions:
            found = board[fy(symbol.y)][fx(symbol.x)]
            if isinstance(found, PartsNumber):
                symbol.add_number(found.number)

def first():
    board, symbols = parse_board()
    find_numbers(board, symbols)
    return sum(num for symbol in symbols for num in symbol.numbers)


def second():
    board, symbols = parse_board()
    find_numbers(board, symbols)
    gears = list(filter(lambda symbol: len(symbol.numbers) == 2, symbols))
    return sum(gear.gear_ratio() for gear in gears)


if __name__ == '__main__':
    result = first()
    assert result == 537732
    print(result)
    result = second()
    assert result == 84883664
    print(result)
