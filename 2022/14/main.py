def parse(file, floor=False):
    with open(file) as f:
        rocks = []
        max_y = 0
        max_x = 0
        min_x = 0
        for line in f.read().split('\n')[:-1]:
            rock = [[int(i) for i in j.split(',')] for j in line.split(' -> ')]
            rock_i = []
            for i, j in zip(rock[:-1], rock[1:]):
                minx = min(i[0], j[0])
                maxx = max(i[0], j[0])
                min_x = min(min_x, minx)
                max_x = max(max_x, maxx)
                x = list(range(minx, maxx+1))
                miny = min(i[1], j[1])
                maxy = max(i[1], j[1])
                max_y = max(max_y, maxy)
                y = list(range(miny, maxy+1))
                for n in x:
                    rock_i.append((n, miny))

                for n in y:
                    rock_i.append((minx, n))

            rocks += list(set(rock_i))

        MAX_Y = max_y+3
        print(max_y)
        print(max_x)
        print(min_x)
        scan = [['.' for i in range(1000)] for i in range(MAX_Y)]
        for x, y in rocks:
            scan[y][x] = '#'

        if floor:
            for i in range(1000):
                scan[max_y + 2][i] = '#'
        # for row in scan:
        #     print(''.join(row))
        falling = True
        counter = 0
        while falling:
            sx, sy = 500, 0
            while True:
                if sy + 1 == MAX_Y:
                    falling = False
                    break
                if scan[sy+1][sx] == '.':
                    sy += 1
                elif scan[sy+1][sx-1] == '.':
                    sy += 1
                    sx -=1
                elif scan[sy+1][sx+1] == '.':
                    sy += 1
                    sx += 1
                else:
                    if scan[sy][sx] == 'o':
                        falling = False
                        break
                    scan[sy][sx] = 'o'
                    counter += 1
                    sx, sy = 500, 0

        for row in scan:
            print(''.join(row[450:650]))
        print("counter: ", counter)


def first(file):
    parse(file)

def second(file):
    parse(file, True)

if __name__ == '__main__':
    # first('test.txt')
    # first('input.txt')
    second('test.txt')
    second('input.txt')
