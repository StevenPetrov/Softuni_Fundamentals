word = input()

while True:
    text = input()
    if text == 'Finish':
        break
    text = text.split()
    command = text[0]

    if command == 'Replace':
        current_char = text[1]
        new_char = text[2]
        word = word.replace(current_char, new_char)
        print(word)

    if command == 'Cut':
        start = int(text[1])
        end = int(text[2])
        if start >= 0 and end <= len(word) and start <= end:
            word = word[:start] + word[end+1:]
            print(word)
        else:
            print("Invalid indices!")

    if command == 'Make':
        com = text[1].lower()
        if com == 'upper':
            word = word.upper()
        else:
            word = word.lower()
        print(word)

    if command == 'Check':
        string_check = text[1]
        if string_check in word:
            print(f"Message contains {string_check}")
        else:
            print(f"Message doesn't contain {string_check}")

    if command == 'Sum':
        start = int(text[1])
        end = int(text[2])
        if start >= 0 and end <= len(word) and start <= end:
            new = word[start:end + 1]
            sum_new = 0
            for x in new:
                sum_new += ord(x)
            print(sum_new)
        else:
            print('Invalid indices!')
