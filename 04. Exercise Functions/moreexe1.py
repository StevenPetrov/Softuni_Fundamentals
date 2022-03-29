def weird(word,num):
    if word == 'int':
        print(int(num)*2)
    elif word == 'real':
        print(f'{int(num)*1.5:.2f}')
    elif word == 'string':
        print(f'${num}$')

weird(input(),input())