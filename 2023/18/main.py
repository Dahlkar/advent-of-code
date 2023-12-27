def get_path(instructions, hex_instructions=False):
    current = (0, 0)
    visited = set()
    path = []
    for d, times, val in instructions:
        times = int(times)
        if hex_instructions:
            hex = val.replace('(', '').replace(')', '').replace('#', '')
            d = hex[-1]
            times = int(hex[:-1], 16)

        x, y = current
        match d:
            case 'U' | '3':
                current = (x, y + times)
            case 'D' | '1':
                current = (x, y - times)
            case 'R' | '0':
                current = (x + times, y)
            case 'L' | '2':
                current = (x - times, y)

        if current in visited:
            continue

        visited.add(current)
        path.insert(0, current)

    return path


def get_area(path):
    n = len(path) - 1
    sum1 = 0
    sum2 = 0

    for i in range(n):
        sum1 = sum1 + path[i][0] * path[i+1][1]
        sum2 = sum2 + path[i][1] * path[i+1][0]

    sum1 = sum1 + path[n][0] * path[0][1]
    sum2 = sum2 + path[0][0] * path[n][1]
    area = abs(sum1 - sum2) // 2

    distance = 0
    for i in range(n):
        distance += abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1])

    distance += abs(path[n][0] - path[0][0]) + abs(path[n][1] - path[0][1])
    return area + distance // 2 + 1


with open('example.txt') as f:
    instructions = [line.split() for line in f.read().splitlines()]
    path = get_path(instructions)
    result = get_area(path)
    print(result)
    assert result == 62
    path = get_path(instructions, True)
    result = get_area(path)
    print(result)
    assert result == 952408144115


with open('input.txt') as f:
    instructions = [line.split() for line in f.read().splitlines()]
    path = get_path(instructions)
    print(get_area(path) + len(path) // 2 + 1)
    path = get_path(instructions, True)
    result = get_area(path)
    print(result)
