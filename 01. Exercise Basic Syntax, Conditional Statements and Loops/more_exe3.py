animals = input()

list = []

for x in animals:
    if x == 's':
        list.append('sheep')
    if x == 'w':
        list.append('wolf')

trigger = True

while trigger:
    if list[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        trigger = False
        break
    count_number = 0
    for x in list:
        count_number +=1
        if x == 'wolf':
            print(f"Oi! Sheep number {len(list)-count_number}! You are about to be eaten by a wolf!" )
            trigger = False
