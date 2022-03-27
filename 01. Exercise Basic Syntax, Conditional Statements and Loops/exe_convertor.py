from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input('Eneter amount: '))
from_currency = input('From Currency: ').upper()
to_currency = input('To Currency: ').upper()

print(amount, from_currency, '<---- TO ----->', to_currency)

result = c.convert(from_currency, to_currency, amount)

print(f'{result:.2f}')
