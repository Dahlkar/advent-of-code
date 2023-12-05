def parse(file):
    with open(file) as f:
        stacks = []
        instructions = []
        is_instructions = False
        for line in f.readlines():
            line = line.replace('\n', '')
            if is_instructions:
                instructions.append(line.replace('move ', '').replace('from ', '').replace('to ', '').split(' '))
            elif line == '':
                is_instructions = True
            else:
                row = {}
                for i, char in enumerate(line):
                    if char not in [' ', '[', ']']:
                        row[i] = char
                stacks.append(row)

        stacks.reverse()
        s = {}
        table = {}
        for row in stacks:
            if s == {}:
                table = row
                s = {
                    k: []
                    for k in row.values()
                }
            else:
                for k, v in row.items():
                    s[table[k]].append(v)
    return s, instructions

def first(file):
    s, instructions = parse(file)
    for m, f, t in instructions:
        m = int(m)
        for i in range(m):
            l = len(s[f])
            s[t].extend(s[f][l-1:])
            s[f] = s[f][:l-1]

    result = ''
    for value in s.values():
        result += value[-1]
    print(result)

def second(file):
    s, instructions = parse(file)
    for m, f, t in instructions:
        m = int(m)
        l = len(s[f])
        s[t].extend(s[f][l-m:])
        s[f] = s[f][:l-m]

    result = ''
    for value in s.values():
        result += value[-1]
    print(result)

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
