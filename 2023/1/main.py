
def first():
    with open('input.txt') as f:
        numbers = []
        for line in f.readlines():
            digits = [s for s in line if s.isdigit()]
            try:
                numbers.append(int(digits[0] + digits[-1]))
            except:
                continue

        print(sum(numbers))

def second():
    words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    with open('input.txt') as f:
        numbers = []
        for line in f.readlines():
            digits = []
            word = ''
            for s in line:
                word += s
                for w in words:
                    if w in word:
                        digits.append(words[w])
                        word = s

                if s.isdigit():
                    digits.append(s)
                    word = ''

            try:
                number = int(digits[0] + digits[-1])
                numbers.append(number)
            except:
                continue

        print(sum(numbers))

if __name__ == '__main__':
    first()
    second()
