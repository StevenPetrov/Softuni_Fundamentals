word = input()
encrypted = ''
for x in word:
    y = ord(x) + 3
    encrypted += chr(y)

print(encrypted)