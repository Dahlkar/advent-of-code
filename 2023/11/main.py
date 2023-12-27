import copy
import itertools


def parse_data(filename, expand=2):
    board = []
    with open(filename) as f:
        for line in f.readlines():
            row = []
            for c in line:
                if c != '\n':
                    row.append(c)

            board.append(row)

    l = len(board)
    b = board.copy()
    expand_y = set()
    for i in range(l):
        row = b[i]
        c = set(row)
        if len(c) == 1:
            expand_y.add(i)

    l = len(board[0])
    r = len(board)
    b = copy.deepcopy(board)
    expand_x = set()
    for i in range(l):
        c = set()
        for row in b:
            c.add(row[i])

        if len(c) == 1:
            expand_x.add(i)

    galaxies = {}
    counter = 0
    print(expand_x)
    for y, row in enumerate(board):
        for x, c in enumerate(row):
            if c == '#':
                x_offset = len([i for i in expand_x if i < x]) * (expand - 1)
                y_offset = len([i for i in expand_y if i < y]) * (expand - 1)
                counter += 1
                galaxies[counter] = (x + x_offset, y + y_offset)
                row[x] = counter

    return galaxies, board

def get_manhattan_distances(galaxies):
    l = list(itertools.combinations(galaxies.values(), 2))
    distances = []
    for (sx, sy), (ex, ey) in l:
        distances.append(abs(sx - ex) + abs(sy - ey))

    return distances


if __name__ == '__main__':
    galaxies, board = parse_data('example.txt')
    distances = get_manhattan_distances(galaxies)
    result = sum(distances)
    print(result)
    assert result == 374
    galaxies, board = parse_data('input.txt')
    distances = get_manhattan_distances(galaxies)
    result = sum(distances)
    print(result)
    galaxies, board = parse_data('example.txt', expand=10)
    distances = get_manhattan_distances(galaxies)
    result = sum(distances)
    print(result)
    assert result == 1030
    galaxies, board = parse_data('example.txt', expand=100)
    distances = get_manhattan_distances(galaxies)
    result = sum(distances)
    print(result)
    assert result == 8410
    galaxies, board = parse_data('input.txt', expand=1000000)
    distances = get_manhattan_distances(galaxies)
    result = sum(distances)
    print(result)
