VOWELS = 'aeiou'

INVALID = ['ab', 'cd', 'pq', 'xy']

def is_nice(string):
    vowels = 0
    double_letter = False
    for invalid in INVALID:
        if invalid in string:
            return False

    for i, c in enumerate(string):
        if i > 0:
            if len(set([string[i-1], c])) == 1:
                double_letter = True

        if c in VOWELS:
            vowels += 1

    return vowels >= 3 and double_letter


def is_nice_two(string):
    ...


if __name__ == '__main__':
    example = [
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb',
    ]
    result = list(filter(is_nice, example))
    with open('input.txt') as f:
        data = [line.replace('\n', '') for line in f.readlines()]
        print(len(list(filter(is_nice, data))))
