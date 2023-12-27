class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'House({self.x}, {self.y})'

    def __repr__(self):
        return str(self)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))

    def left(self):
        return House(self.x - 1, self.y)

    def right(self):
        return House(self.x + 1, self.y)

    def up(self):
        return House(self.x, self.y + 1)

    def down(self):
        return House(self.x, self.y - 1)


def track_path(path):
    current_position = House(0, 0)
    houses = {current_position}
    for d in path:
        match d:
            case '>':
                current_position = current_position.right()
            case '<':
                current_position = current_position.left()
            case '^':
                current_position = current_position.up()
            case 'v':
                current_position = current_position.down()
            case _:
                break

        houses.add(current_position)

    return len(houses)


def direction(house, d):
    match d:
        case '>':
            return house.right()
        case '<':
            return house.left()
        case '^':
            return house.up()
        case 'v':
            return house.down()
        case _:
            pass


def track_path_two(path):
    santa_position = House(0, 0)
    houses = {santa_position}
    robo_position = House(0, 0)

    for i, d in enumerate(path):
        if d == '\n':
            break
        if i % 2 == 0:
            santa_position = direction(santa_position, d)
            houses.add(santa_position)
        else:
            robo_position = direction(robo_position, d)
            houses.add(robo_position)

    return len(houses)

if __name__ == '__main__':
    with open('input.txt') as f:
        path = f.read()
        result = track_path(path)
        print(result)
        assert result == 2081
        result = track_path_two(path)
        print(result)
        assert result == 2341
