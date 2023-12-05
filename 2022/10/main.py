def parse(file):
    with open(file) as f:
        return [[i for i in line.split(' ')] for line in f.read().split('\n')[:-1]]

def first(file):
    instructions = parse(file)
    cycles = 0
    X = 1
    signals = []
    ops = {
        'noop': 1,
        'addx': 2,
    }
    screen = [['.' for i in range(40)] for i in range(6)]
    for ins in instructions:
        op = ins[0]
        for i in range(ops[op]):
            if X-1 <= cycles % 40 <= X+1:
                screen[cycles // 40][cycles % 40] = '#'
            cycles += 1
            if cycles in [20, 60, 100, 140, 180, 220]:
                signals.append(X * cycles)
            # print(cycles // 40)
            # print(X % 40)
        if op == 'addx':
            X = X + int(ins[1])

    print(signals)
    print(sum(signals))
    for row in screen:
        print(''.join(row))

def second(file):
    pass

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test2.txt')
    second('input.txt')
