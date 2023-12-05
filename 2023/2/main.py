from functools import reduce


def first():
    rules = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    with open('input.txt') as f:
        valid_games = []
        for line in f.readlines():
            game, rounds = line.split(':')
            _, id = game.split()
            sets = rounds.split(';')
            valid = True
            for set in sets:
                for x in set.split(','):
                    num, color = x.split()
                    if int(num) > rules[color]:
                        valid = False

            if valid:
                valid_games.append(int(id))

        print(sum(valid_games))


def second():
    with open('input.txt') as f:
        powers = []
        for line in f.readlines():
            game, rounds = line.split(':')
            _, id = game.split()
            sets = rounds.split(';')
            d = {}
            for set in sets:
                for x in set.split(','):
                    num, color = x.split()
                    tmp = d.get(color, 0)
                    d[color] = tmp if tmp > int(num) else int(num)

            powers.append(reduce((lambda x, y: x * y), list(d.values())))

        print(sum(powers))


if __name__ == '__main__':
    first()
    second()
