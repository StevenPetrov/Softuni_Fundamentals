l = input().split()
n = []
for x in l:
    number = int(x[1:-1])
    if x[0].isupper():
        letter_position = ord(x[0]) - 64
        number /= letter_position
    if x[0].islower():
        letter_position = ord(x[0]) - 96
        number *= letter_position
    if x[-1].isupper():
        letter_position = ord(x[-1]) - 64
        number -= letter_position
    if x[-1].islower():
        letter_position = ord(x[-1]) - 96
        number += letter_position
    n.append(number)

print(f'{sum(n):.2f}')