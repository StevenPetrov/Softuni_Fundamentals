d = {}

while True:
    command = input()
    if command == 'statistics':
        break
    command = command.split(': ')
    product = command[0]
    value = int(command[1])
    if product in d:
        d[product] += value
    else:
        d[product] = value

print(f'Products in stock:')
products_count = len(d.keys())
quantity_count = sum(d.values())
for x in d:
    print(f'- {x}: {d[x]}')
#     products_count += 1
#     quantity_count += int(d[x])
print(f'Total Products: {products_count}')
print(f'Total Quantity: {quantity_count}')
