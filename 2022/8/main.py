def parse(file):
    with open(file) as f:
        grid = [[int(t) for t in line] for line in f.read().split('\n')[:-1]]

    visible = 0
    scores = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1:
                visible += 1
                continue

            height = grid[x][y]
            west_grid = grid[x][:y]
            east_grid = grid[x][y+1:]
            north_grid = grid[:x]
            south_grid = grid[x+1:]
            west = max(west_grid)
            east = max(east_grid)
            north = max([line[y] for line in north_grid])
            south = max([line[y] for line in south_grid])
            if west < height or east < height or north < height or south < height:
                visible += 1

            score = 1
            west_grid.reverse()
            north_grid.reverse()
            s = True
            for i in range(len(west_grid)):
                if west_grid[i] >= height:
                    s = False
                    score *= i+1
                    break
            if s:
                score *= len(west_grid)

            s = True
            for i in range(len(east_grid)):
                if east_grid[i] >= height:
                    s = False
                    score *= i+1
                    break

            if s:
                score *= len(east_grid)

            s = True
            for i in range(len(north_grid)):
                if north_grid[i][y] >= height:
                    s = False
                    score *= i+1
                    break

            if s:
                score *= len(north_grid)

            s = True
            for i in range(len(south_grid)):
                if south_grid[i][y] >= height:
                    s = False
                    score *= i+1
                    break
            if s:
                score *= len(south_grid)

            scores.append(score)
    print(visible)
    print(max(scores))

def first(file):
    parse(file)

def second(file):
    pass

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
