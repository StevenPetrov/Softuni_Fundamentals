positive = list()
negative = list()
even = list()
odd = list()

l = list(map(int,input().split(', ')))

lmao = [even.append(str(x)) if x % 2 == 0 else odd.append(str(x)) for x in l]
lmao = [positive.append(str(x)) if x >= 0 else negative.append(str(x)) for x in l]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')