l = input().split('|')
budget = float(input())
profit = 0
new_prices = []
new_prices_str = []
condition = False

for x in l:
    word = x.split('->')
    price = float(word[1])
    condition = False
    if 'Clothes' == word[0] and price <= 50:
            condition = True
    elif 'Shoes' == word[0] and price <= 35:
            condition = True
    elif 'Accessories' == word[0] and price <= 20.50:
            condition = True
    if condition:
        if budget >= price:
            budget -= price
            new_price = price * 0.4 + price
            new_prices.append(new_price)
            new_prices_str.append(f'{new_price:.2f}')
            profit += (new_price - price)


all = sum(new_prices)
print(' '.join(new_prices_str))
print(f'Profit: {profit:.2f}')
if all+profit+budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
