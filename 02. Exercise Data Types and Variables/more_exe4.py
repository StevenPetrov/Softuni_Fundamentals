lines = int(input())
right = 0
left = 0
char = ''
trigger = False
first_brake = False

for x in range(lines):
    if left > right:
        trigger = False
    enter = input()
    if enter == '(':
        if char == enter:
            trigger = True
        right += 1
        char = enter
    if enter == ')':
        if char == enter:
            trigger = True
        left += 1
        char = enter

if lines > 0:
    if trigger or right != left:
        print("UNBALANCED")
    else:
        print("BALANCED" )