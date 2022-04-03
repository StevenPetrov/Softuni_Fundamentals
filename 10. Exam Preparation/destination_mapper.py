import re

countries = []
filtered = []
text = input()

pattern = r'=([A-Z][A-Za-z][A-Za-z]+)=|/([A-Z][A-Za-z][A-Za-z]+)/'

l = re.finditer(pattern,text)

for x in l:
    countries.append(x.group())

travel_points = 0

for x in countries:
    word = x[1:-1]
    filtered.append(word)
    travel_points += len(word)

print(f'Destinations: {", ".join(filtered)}')
print(f'Travel Points: {travel_points}')