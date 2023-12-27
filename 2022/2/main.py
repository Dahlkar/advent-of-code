from enum import IntEnum

class Choices(IntEnum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

class Hands(IntEnum):
    A = 1
    B = 2
    C = 3

    @classmethod
    def _missing_(cls, value):
        if value == 0:
            return cls(3)
        elif value == 4:
            return cls(1)


def first(file):
    with open(file) as f:
        score = 0
        for line in f.readlines():
            x, y = line.strip('\n').split(' ')
            elf = Choices[x]
            me = Choices[y]
            result = elf - me
            if result == 0:
                score += 3 + me
            elif result == -1 or result == 2:
                score += 6 + me
            else:
                score += me
        print(score)


def second(file):
    with open(file) as f:
        score = 0
        for line in f.readlines():
            x, y = line.strip('\n').split(' ')
            elf = Hands[x]
            if y == 'X':
                me = Hands(elf - 1)
                score += me
            elif y == 'Y':
                score += 3 + elf
            elif y == 'Z':
                me = Hands(elf + 1)
                score += 6 + me

        print(score)

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
