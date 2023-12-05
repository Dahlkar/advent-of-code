import json
import functools
import operator


def parse(file):
    with open(file) as f:
        pairs = []
        pair = []
        for line in f.read().split('\n'):
            if line != '':
                pair.append(json.loads(line))
            else:
                pairs.append(pair)
                pair = []

    return pairs

def check(left, right):
    for l, r in zip(left, right):
        if isinstance(l, list) and isinstance(r, list):
            result = check(l, r)
            if result == 0:
                continue
            return result
        elif isinstance(l, list):
            result = check(l, [r])
            if result == 0:
                continue
            return result
        elif isinstance(r, list):
            result = check([l], r)
            if result == 0:
                continue
            return result
        if l == r:
            continue
        elif l < r:
            return -1
        elif l > r:
            return 1

    if len(left) < len(right):
        return -1
    elif len(right) < len(left):
        return 1

    return 0

def first(file):
    pairs = parse(file)
    correct = []
    i = 1
    for pair in pairs:
        result = check(*pair)
        if result < 0:
            correct.append(i)

        i += 1
    print(correct)
    print(sum(correct))

def second(file):
    pairs = parse(file)
    packets = []
    for pair in pairs:
        packets += pair

    packets += [[[2]], [[6]]]
    sorted_pairs = sorted(packets, key=functools.cmp_to_key(check))
    divider_index = []
    for i, packet in enumerate(sorted_pairs, start=1):
        if len(divider_index) == 2:
            break
        if packet == [[2]]:
            divider_index.append(i)
        elif packet == [[6]]:
            divider_index.append(i)

    print(operator.mul(*divider_index))
if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
