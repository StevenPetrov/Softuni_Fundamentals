fire_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for x in fire_cells:
    if 'High' in x:
        level = x[-3:]
        level = int(level)
        if 80 < level <= 125:
            if water - level >= 0:
                water -= level
                effort += level*0.25
                total_fire += level
                print(f' - {level}')
    if 'Medium' in x:
        level = x[-2:]
        level = int(level)
        if 50 < int(level) <= 80:
            if water - level >= 0:
                water -= level
                effort += level*0.25
                total_fire += level
                print(f' - {level}')
    if 'Low' in x:
        level = x[-2:]
        level = int(level)
        if 0 < int(level) <= 50:
            if water - level >= 0:
                water -= level
                effort += level*0.25
                total_fire += level
                print(f' - {level}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')