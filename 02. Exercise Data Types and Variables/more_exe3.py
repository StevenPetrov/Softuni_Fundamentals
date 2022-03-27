key = int(input())
lines = int(input())

for x in range(lines):
    letter = ord(input())
    print(chr(letter+key), end='')