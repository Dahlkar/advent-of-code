from hashlib import md5




if __name__ == '__main__':
    input = 'iwrupvqb'
    target = '00000000000000000'
    counter = 0
    not_found_six = True
    found_five = False
    while not_found_six:
        hash = md5(f'{input}{counter}'.encode()).hexdigest()
        if not found_five and hash[:5] == target[:5]:
            print(counter)
            found_five = True
        if hash[:6] == target[:6]:
            print(counter)
            not_found_six = False
        counter += 1
