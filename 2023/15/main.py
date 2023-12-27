from collections import OrderedDict

def hash(s):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result = result % 256

    return result


def order_lenses(instructions):
    boxes = {}
    for instruction in instructions.split(','):
        if '=' in instruction:
            key, lens = instruction.split('=')
            hkey = hash(key)
            box = boxes.get(hkey, OrderedDict())
            box[key] = int(lens)
            boxes[hkey] = box
        if '-' in instruction:
            key, _ = instruction.split('-')
            hkey = hash(key)
            box = boxes.get(hkey, {})
            if key in box:
                box.pop(key)
            boxes[hkey] = box

    return boxes

def focusing_power(boxes):
    result = 0
    for k, box in boxes.items():
        bi = k + 1
        for i, l in enumerate(box.values(), start=1):
            power = bi * i * l
            result += power

    return result


if __name__ == '__main__':
    input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    result = sum(hash(w) for w in input.split(','))
    print(result)
    assert result == 1320
    boxes = order_lenses(input)
    result = focusing_power(boxes)
    print(result)
    with open('input.txt') as f:
        lines = f.read().splitlines()
        result = sum(hash(w) for w in lines[0].split(','))
        print(result)
        boxes = order_lenses(lines[0])
        result = focusing_power(boxes)
        print(result)
