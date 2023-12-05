def parse(file):
    with open(file) as f:
        return [[i for i in line.split(' ')] for line in f.read().split('\n')[:-1]]


def first(file):
    instructions = parse(file)
    h_pos = [0, 0]
    t_pos = [0, 0]
    t_visited = [(0, 0)]
    for d, s in instructions:
        for i in range(int(s)):
            if d == 'R':
                h_pos[0] = h_pos[0] + 1
                if abs(h_pos[0]-t_pos[0]) > 1:
                    t_pos[0] = t_pos[0] + 1
                    if h_pos[1] != t_pos[1]:
                        t_pos[1] = h_pos[1]
                    t_visited.append(tuple(t_pos))
            if d == 'L':
                h_pos[0] = h_pos[0] - 1
                if abs(h_pos[0]-t_pos[0]) > 1:
                    t_pos[0] = t_pos[0] - 1
                    if h_pos[1] != t_pos[1]:
                        t_pos[1] = h_pos[1]
                    t_visited.append(tuple(t_pos))
            if d == 'U':
                h_pos[1] = h_pos[1] + 1
                if abs(h_pos[1]-t_pos[1]) > 1:
                    t_pos[1] = t_pos[1] + 1
                    if h_pos[0] != t_pos[0]:
                        t_pos[0] = h_pos[0]
                    t_visited.append(tuple(t_pos))
            if d == 'D':
                h_pos[1] = h_pos[1] - 1
                if abs(h_pos[1]-t_pos[1]) > 1:
                    t_pos[1] = t_pos[1] - 1
                    if h_pos[0] != t_pos[0]:
                        t_pos[0] = h_pos[0]
                    t_visited.append(tuple(t_pos))
    print(len(set(t_visited)))

def second(file):
    instructions = parse(file)
    rope = [[0, 0] for i in range(10)]
    t_visited = [(0, 0)]
    for d, s in instructions:
        for i in range(int(s)):
            if d == 'R':
                rope[0][0] = rope[0][0] + 1
            if d == 'L':
                rope[0][0] = rope[0][0] - 1
            if d == 'U':
                rope[0][1] = rope[0][1] + 1
            if d == 'D':
                rope[0][1] = rope[0][1] - 1

            for i, knot in enumerate(rope[1:]):
                xh, yh = rope[i]
                xt, yt = knot
                dx = abs(xh - xt)
                dy = abs(yh - yt)
                if dx <= 1 and dy == 2:
                    knot = (xh, yh - (yh - yt) // dy)
                elif dx == 2 and dy <= 1:
                    knot = (xh - (xh - xt) // dx, yh)
                elif dx == 2 and dy == 2:
                    knot = (xh - (xh - xt) // dx, yh - (yh - yt) // dy)

                rope[i+1] = knot

            t_visited.append(tuple(rope[-1]))


    print(len(set(t_visited)))
    return t_visited

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test2.txt')
    second('input.txt')
