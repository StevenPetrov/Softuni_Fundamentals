word1 = input()
word2 = input()

current_word= word1
last_printed_word = word1

for x in range(len(word1)):
    current_word_symbol = word2[x]
    current_word = current_word[:x] + current_word_symbol + current_word[x+1:]
    if current_word != last_printed_word:
        print(current_word)
        last_printed_word = current_word


#slice notation
