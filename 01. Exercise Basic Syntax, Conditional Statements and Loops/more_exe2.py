word = input()

list = []
word_count = -1

for x in word:
    word_count += 1
    if x.isupper():
        list.append(word_count)

print(list)