import re

text = input()
word = input()
word_reg = ''

for x in word:
    word_reg += '[' + x + ']'

pattern = r'\b' + word_reg + r'\b'

repeated = re.findall(pattern, text, re.IGNORECASE)

print(len(repeated))
