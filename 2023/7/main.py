from collections import Counter

cards = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'j': 1,
}

class Hand:
    def __init__(self, hand, bid, joker=False):
        self.hand = hand
        self.bid = bid
        if joker:
            self.hand = hand.replace('J', 'j')
        self.value = self.get_hand_value(joker)

    def get_hand_value(self, joker):
        counter = Counter(self.hand)
        if joker:
            joker_count = counter['j']
            del counter['j']
            try:
                most_common = counter.most_common(1)[0][0]
            except IndexError:
                most_common = 'j'
            counter[most_common] += joker_count

        match sorted(list(counter.values())):
            case [1, 1, 1, 1, 1]:
                return 1
            case [1, 1, 1, 2]:
                return 2
            case [1, 2, 2]:
                return 3
            case [1, 1, 3]:
                return 4
            case [2, 3]:
                return 5
            case [1, 4]:
                return 6
            case [5]:
                return 7

    def __lt__(self, o):
        if self.value != o.value:
            return self.value < o.value

        for c, oc in zip(self.hand, o.hand):
            if cards[c] != cards[oc]:
                return cards[c] < cards[oc]

    def __str__(self):
        return f'Hand({self.hand}, {self.bid}, {self.value})'

    def __repr__(self):
        return str(self)


def parse_data(filename, joker=False):
    hands = []
    with open(filename) as f:
        for line in f.readlines():
            hand, bid = line.split()
            hands.append(Hand(hand, int(bid), joker))

    return hands

def get_winnings(hands):
    hands.sort()
    print(hands)
    return sum(i * h.bid for i, h in enumerate(hands, start=1))


if __name__ == '__main__':
    hands = parse_data('example.txt')
    result = get_winnings(hands)
    print(result)
    assert result == 6440
    hands = parse_data('input.txt')
    result = get_winnings(hands)
    print(result)
    assert result == 250254244
    hands = parse_data('example.txt', joker=True)
    result = get_winnings(hands)
    print(result)
    assert result == 5905
    hands = parse_data('input.txt', joker=True)
    result = get_winnings(hands)
    print(result)
    assert result == 250087440
