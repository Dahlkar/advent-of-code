def main(n):
    with open('input.txt') as f:
        calories = []
        current_calories = 0
        for line in f.readlines():
            if line != '\n':
                current_calories += int(line.strip('\n'))
            else:
                calories.append(current_calories)
                current_calories = 0

        calories.sort(reverse=True)
        print(sum(calories[:n]))

if __name__ == '__main__':
    main(1)
    main(3)
