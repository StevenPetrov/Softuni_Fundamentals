coded = input().split(' ')
numcode = []
for x in coded:
    counter = 0
    alpha_counter = 0
    for y in x:
        if y.isalpha():
            alpha_counter +=1
        if y.isdigit():
            numcode.append(y)
            counter +=1
    letter_decode = chr(int(''.join(numcode)))
    a = x[counter]
    b = x[-1]
    a,b = b,a
    if alpha_counter <2:
        print(f'{letter_decode}{a}', end=' ')
    else:
        print(f'{letter_decode}{a}{x[counter+1:-1]}{b}', end=' ')
    numcode = []