#!/usr/bin/env python
from dataclasses import dataclass

north = {'|', 'F', '7'}
south = {'|', 'J', 'L'}
west = {'-', 'F', 'L'}
east = {'-', 'J', '7'}


rules = {
    '|': {
        'n': north,
        's': south,
    },
    '-': {
        'w': west,
        'e': east,
    },
    'F': {
        's': south,
        'e': east,
    },
    '7': {
        's': south,
        'w': west,
    },
    'L': {
        'n': north,
        'e': east,
    },
    'J': {
        'n': north,
        'w': west,
    },
    'S': {
        'n': north,
        's': south,
        'w': west,
        'e': east,
    }
}


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def north(self):
        return Point(self.x, self.y - 1)

    def south(self):
        return Point(self.x, self.y + 1)

    def west(self):
        return Point(self.x - 1, self.y)

    def east(self):
        return Point(self.x + 1, self.y)


class Pipe:
    type: str
    point: Point

    def __init__(self, type, point):
        self.type = type
        self.point = point
        self.neighbors = []

    def __hash__(self):
        return hash(self.point)

    def get_neighbors(self, board):
        if not self.neighbors:
            for d, rule in rules[self.type].items():
                match d:
                    case 'n':
                        neighbor = board[self.point.north()]
                    case 's':
                        neighbor = board[self.point.south()]
                    case 'w':
                        neighbor = board[self.point.west()]
                    case 'e':
                        neighbor = board[self.point.east()]

                if neighbor.type in rule:
                    self.neighbors.append(neighbor)

        return self.neighbors

    def __repr__(self):
        return f'Pipe({self.type}, {self.point})'


class Board:
    def __init__(self):
        self.board = []

    def __getitem__(self, point):
        return self.board[point.y][point.x]

    def append(self, item):
        self.board.append(item)

    def __iter__(self):
        for row in self.board:
            yield row

    def __str__(self):
        s = ''
        for row in self.board:
            s += ''.join(p.type for p in row)

        return s


def parse_data(filename):
    start = None
    board = Board()
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            row = []
            for j, c in enumerate(line):
                point = Point(j, i)
                pipe = Pipe(c, point)
                row.append(pipe)
                if c == 'S':
                    start = pipe

            board.append(row)

        return start, board


def get_pipe_maze(start, board):
    visited = set()
    pipe_maze = list()
    queue = list([start])

    while queue:
        n = queue.pop()
        visited.add(n)
        pipe_maze.append(n)
        for neighbor in n.get_neighbors(board):
            if neighbor not in visited:
                queue.append(neighbor)

    return pipe_maze


def get_pipe_maze_area(pipe_maze):
    vertices = list(pipe_maze)
    n = len(pipe_maze) - 1
    sum1 = 0
    sum2 = 0

    for i in range(n):
        sum1 = sum1 + pipe_maze[i].point.x * pipe_maze[i+1].point.y
        sum2 = sum2 + pipe_maze[i].point.y * pipe_maze[i+1].point.x

    sum1 = sum1 + pipe_maze[n].point.x * vertices[0].point.y
    sum2 = sum2 + vertices[0].point.x * vertices[n].point.y
    area = abs(sum1 - sum2) / 2
    return area


def interior_points(pipe_maze):
    area = get_pipe_maze_area(pipe_maze)
    return int(area - (len(pipe_maze) // 2) + 1)


if __name__ == '__main__':
    start, board = parse_data('input.txt')
    pipe_maze = get_pipe_maze(start, board)
    result = len(pipe_maze) // 2
    print(result)
    assert result == 6640
    result = interior_points(pipe_maze)
    print(result)
    assert result == 411
