def get_points(filename):
    with open(filename) as f:
        score = 0
        for line in f.readlines():
            line = line.replace('\n', '')
            card, numbers = line.split(':')
            winning_numbers, card_numbers = numbers.split('|')
            winning_numbers = set(num for num in winning_numbers.split(' ') if num != '')
            card_numbers = set(num for num in card_numbers.split(' ') if num != '')
            score_numbers = winning_numbers.intersection(card_numbers)
            if score_numbers:
                card_score = 2**(len(score_numbers) - 1)
                score += card_score

        return int(score)


def calc_winnings(filename):
    with open(filename) as f:
        scratchcards = {}
        for line in f.readlines():
            line = line.replace('\n', '')
            card, numbers = line.split(':')
            try:
                _, card_id = card.split()
            except :
                print(card)
                raise
            winning_numbers, card_numbers = numbers.split('|')
            winning_numbers = set(num for num in winning_numbers.split(' ') if num != '')
            card_numbers = set(num for num in card_numbers.split(' ') if num != '')
            score_numbers = winning_numbers.intersection(card_numbers)
            scratchcards[int(card_id)] = {
                'num': 1,
                'winnings': len(score_numbers),
            }

        for card_id, value in scratchcards.items():
            for j in range(value['num']):
                for i in range(card_id + 1, card_id + value['winnings'] + 1):
                    scratchcards[i]['num'] += 1


        return sum(c['num'] for c in scratchcards.values())


if __name__ == '__main__':
    result = get_points('example.txt')
    print(result)
    assert result == 13
    result = get_points('input.txt')
    print(result)
    result = calc_winnings('example.txt')
    print(result)
    assert result == 30
    result = calc_winnings('input.txt')
    print(result)
