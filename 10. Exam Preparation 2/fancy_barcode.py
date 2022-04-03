import re


times = int(input())
pattern = r'^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$'


for x in range(times):
    text = input()
    barcode = re.findall(pattern,text)
    if len(barcode) == 1:
        for y in barcode:
            digits = ''
            for z in y:
                if z in ("1234567890"):
                    digits += z
            if digits == '':
                print('Product group: 00')
            else:
                print(f'Product group: {int(digits)}')
    else:
        print('Invalid barcode')