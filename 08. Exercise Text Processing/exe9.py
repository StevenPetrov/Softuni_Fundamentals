word = input()
breaker_check = 0
master = []
counter = -1
final = ''
for x in word:
    counter += 1
    if counter == len(word)-1:
        xx = word[breaker_check:counter+1]
        master.append(xx)
    elif x.isdigit() and word[counter+1] not in '12345678901011121314151617181920':
        xx = word[breaker_check:counter+1]
        master.append(xx)
        breaker_check = counter+1

for x in master:
    number = ''
    text = ''
    for y in x:
        if y.isdigit():
            number += y
        else:
            text += y
    final += text.upper() * int(number)

symbols_counter = len(set(final))


print(f'Unique symbols used: {symbols_counter}')
print(final)