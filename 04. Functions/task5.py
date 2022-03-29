def money_calc(product, order):
    if product == 'coffee':
        return order * 1.5
    elif product == 'water':
        return order * 1
    elif product == 'coke':
        return order * 1.4
    elif product == 'snacks':
        return order * 2


print(f'{money_calc(input(), int(input())):.2f}')
   