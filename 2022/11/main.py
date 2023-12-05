import operator
from math import lcm
ops = {
    "+": operator.add,
    "*": operator.mul,
}
def calculate_worry(operation, item):
    op = None
    args = []
    for i in operation:
        if i == 'old':
            args.append(item)
        elif i in ops:
            op = ops[i]
        else:
            args.append(int(i))
    result = op(*args)
    # print(f"Worry level is multiplied by {args[1]} to {result}")
    # if div != 1:
    #     result = int(result/div)
    # print(f"Monkey gets bored with item. Worry level is divided by {div} to {result}")
    return result

def parse(file, rounds=20):
    with open(file) as f:
        monkeys = {}
        name = ''
        for line in f.read().split('\n')[:-1]:
            if line.startswith('Monkey'):
                name = line.split(' ')[1][0]
                monkeys[name] = {'test': {}, 'inspections': 0}
            elif line.startswith('  Starting'):
                items = line.split('Starting items: ')[1].split(', ')
                monkeys[name]['items'] = [int(i) for i in items]
            elif line.startswith('  Operation'):
                operation = line.split('Operation: ')[1].split('new = ')[1].split(' ')
                monkeys[name]['operation'] = operation
            elif line.startswith('  Test:'):
                test = line.split('Test: divisible by ')[1]
                monkeys[name]['test']['mod'] = int(test)
            elif line.startswith('    If true:'):
                monkey = line.split('If true: throw to monkey ')[1]
                monkeys[name]['test'][True] = monkey
            elif line.startswith('    If false:'):
                monkey = line.split('If false: throw to monkey ')[1]
                monkeys[name]['test'][False] = monkey

    return monkeys

def solve(monkeys, rounds, post_inspection):
    for i in range(rounds):
        for name, monkey in monkeys.items():
            # print("Monkey: ", name)
            for item in monkey['items']:
                monkey['inspections'] += 1
                # print("Monkey inspects an item with a worry level of ", item)
                worry = calculate_worry(monkey['operation'], item)
                worry = post_inspection(worry)
                mod = monkey['test']['mod']
                test = worry % mod == 0
                word = ''
                if not test:
                    word = 'not '
                # print(f'Current worry level is {word}divisible by {mod}.')
                throw = monkey['test'][test]
                # print(f'Item with worry level {worry} is thrown to monkey {throw}.')
                monkeys[throw]['items'].append(worry)
                # print("=" * 20)

            monkey['items'] = []

        # print(monkeys)
    inspections = [m['inspections'] for m in monkeys.values()]
    inspections.sort(reverse=True)
    print(operator.mul(inspections[0], inspections[1]))

if __name__ == '__main__':
    monkeys = parse('test.txt')
    solve(monkeys, 20, lambda x: x / 3)
    monkeys = parse('test.txt')
    base = lcm(*(m['test']['mod'] for m in monkeys.values()))
    solve(monkeys, 10000, lambda x: x % base)
    monkeys = parse('input.txt')
    solve(monkeys, 20, lambda x: x // 3)
    monkeys = parse('input.txt')
    base = lcm(*(m['test']['mod'] for m in monkeys.values()))
    solve(monkeys, 10000, lambda x: x % base)
