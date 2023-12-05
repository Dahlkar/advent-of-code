def first(file):
    with open(file) as f:
        pairs = [
            [
                [int(i) for i in a.split('-') if i != '']
                for a in line.split(',') if a != '']
            for line in f.read().split('\n') if line != '']
        count = 0
        for (i, j), (n, m) in pairs:
            s1 = set(range(i, j+1))
            s2 = set(range(n, m+1))
            if s1 <= s2 or s2 <= s1:
                count += 1

        print(count)

def second(file):
    with open(file) as f:
        pairs = [
            [
                [int(i) for i in a.split('-') if i != '']
                for a in line.split(',') if a != '']
            for line in f.read().split('\n') if line != '']
        count = 0
        for (i, j), (n, m) in pairs:
            s1 = set(range(i, j+1))
            s2 = set(range(n, m+1))
            if s1 & s2:
                count += 1

        print(count)

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
