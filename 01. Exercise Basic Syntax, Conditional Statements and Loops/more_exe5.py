coffee_counter = 0

while True:
    action = input()
    if action == 'END':
        print(coffee_counter)
        break
    if action == 'dog':
        coffee_counter += 1
    if action == 'DOG':
        coffee_counter += 2
    if action == 'cat':
        coffee_counter += 1
    if action == 'CAT':
        coffee_counter += 2
    if action == 'coding':
        coffee_counter += 1
    if action == 'CODING':
        coffee_counter += 2
    if action == 'movie':
        coffee_counter += 1
    if action == 'MOVIE':
        coffee_counter += 2
    if coffee_counter > 5:
        print('You need extra sleep')
        break
