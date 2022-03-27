lines = int(input())
tank = 0

for x in range(lines):
    liters = int(input())
    if tank + liters > 255:
        print("Insufficient capacity!")
    else:
        tank += liters
print(tank)