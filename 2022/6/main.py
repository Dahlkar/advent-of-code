
def first(file):
    with open(file) as f:
        packet = f.read()
        for i in range(4, len(packet)):
            marker = set(packet[i-4:i])
            if len(marker) == 4:
                print(i)
                break

def second(file):
    with open(file) as f:
        packet = f.read()
        for i in range(14, len(packet)):
            marker = set(packet[i-14:i])
            if len(marker) == 14:
                print(i)
                break

if __name__ == '__main__':
    first('test.txt')
    first('input.txt')
    second('test.txt')
    second('input.txt')
