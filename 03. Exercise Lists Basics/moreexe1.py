l = input().split(', ')
lzero = []

while '0' in l: lzero.append('0'), l.remove('0')

l.extend(lzero)

l = list(map(int, l))
print(l)