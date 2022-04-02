digits = []
letters = []
chars = []

word = input()

for x in word:
    if x.isdigit():
        digits.append(x)
    elif x.isalpha():
        letters.append(x)
    else:
        chars.append(x)

print(''.join(digits))
print(''.join(letters))
print(''.join(chars))