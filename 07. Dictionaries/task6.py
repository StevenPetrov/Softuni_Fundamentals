l = input().lower().split()
d ={}
for x in l:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

odd = []

for x in d:
    if d[x] % 2 != 0:
        odd.append(x)

print(' '.join(odd))
