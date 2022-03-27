word = input()

words = 0

word_checker = -1
for x in word.upper():
    word_checker += 1
    if word_checker +1 == len(word):
        break
    if x == 'S':
        if word.upper()[word_checker + 1] == 'A':
            if word.upper()[word_checker + 2] == 'N':
                if word.upper()[word_checker + 3] == 'D':
                    words += 1
    if x == 'W':
        if word.upper()[word_checker + 1] == 'A':
            if word.upper()[word_checker + 2] == 'T':
                if word.upper()[word_checker + 3] == 'E':
                    if word.upper()[word_checker + 4] == 'R':
                        words += 1
    if x == 'F':
        if word.upper()[word_checker + 1] == 'I':
            if word.upper()[word_checker + 2] == 'S':
                if word.upper()[word_checker + 3] == 'H':
                    words += 1
    if x == 'S':
        if word.upper()[word_checker + 1] == 'U':
            if word.upper()[word_checker + 2] == 'N':
                words += 1

print(words)