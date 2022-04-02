import re
total_spend = 0
names = []

while True:
    command = input()
    if command == 'Purchase':
        break
    pattern = r'>>(?P<name>[a-zA-Z]+)<<(?P<price>\d+[.]*\d+\b)!(?P<quantity>\d+\b)'

    brick = re.finditer(pattern,command)

    for x in brick:
        names.append(x.group('name'))
        price = x.group('price')
        quantity = x.group('quantity')
        total_spend += float(price) * int(quantity)

print('Bought furniture:')
print('\n'.join(names))
print(f'Total money spend: {total_spend:.2f}')