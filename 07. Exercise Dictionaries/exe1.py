word = input()
d = {}

for x in word:
    if x != ' ':
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

for x in d:
    print(f'{x} -> {d[x]}')