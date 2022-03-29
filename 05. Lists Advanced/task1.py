vowels = ['a', 'o', 'u', 'e', 'i']

list = [x for x in input() if x.lower() not in vowels]

print(''.join(list))