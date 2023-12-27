from functools import reduce


def parse_data(filename):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            numbers = [int(n) for n in line.split()]
            l = [numbers]
            while not all(d == 0 for d in numbers):
                numbers = [i - j for j, i in zip(numbers[:-1], numbers[1:])]
                l.append(numbers)


            data.append(l)
        return data


def next_numbers(data):
    numbers = []
    for sequences in data:
        numbers.append(sum(sequence[-1] for sequence in sequences))

    return sum(numbers)


def prev_numbers(data):
    numbers = []
    for sequences in data:
        num = 0
        for x in reversed(sequences):
            num = x[0] - num
        numbers.append(num)

    return sum(numbers)

if __name__ == '__main__':
    data = parse_data('example.txt')
    result = next_numbers(data)
    print(result)
    assert result == 114
    data = parse_data('input.txt')
    result = next_numbers(data)
    print(result)
    data = parse_data('example.txt')
    result = prev_numbers(data)
    print(result)
    assert result == 2
    data = parse_data('input.txt')
    result = prev_numbers(data)
    print(result)
