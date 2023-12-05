from enum import Enum
import string


Priority = {l:i
            for i, l in enumerate(
                    string.ascii_lowercase + string.ascii_uppercase, start=1)}

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def first(file):
    with open(file) as f:
        priorities = []
        for line in f.readlines():
            rucksack = line.strip('\n')
            c1, c2 = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
            intersection = c1.intersection(c2)
            priorities.append(Priority[intersection.pop()])
        print(sum(priorities))

def second(file):
    with open(file) as f:
        priorities = []
        lines = [set(line.strip('\n')) for line in f.readlines()]
        groups = divide_chunks(lines, 3)
        for group in groups:
            intersection = set.intersection(*group)
            priorities.append(Priority[intersection.pop()])
        print(sum(priorities))

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
