word1 = input()
word2 = input()

temp_word = word2

while word1 in temp_word:
    temp_word = temp_word.replace(word1, '')

print(temp_word)