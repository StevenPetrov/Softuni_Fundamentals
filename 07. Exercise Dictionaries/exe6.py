d = {}

while True:
    command = input()
    if command == 'buy':
        break
    command = command.split()
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if name not in d:
        d[name] = {'price': price, 'quantity': quantity}
    else:
        d[name]['price'] = price
        d[name]['quantity'] += quantity

for x in d:
    total_sum = d[x]['price'] * d[x]['quantity']
    print(f'{x} -> {total_sum:.2f}')