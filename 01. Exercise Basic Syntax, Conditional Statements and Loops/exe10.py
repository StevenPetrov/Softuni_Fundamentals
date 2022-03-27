quantity = int(input())
days = int(input())

ornaments_price = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

budget = 0
totalSpirit = 0

for day_number in range(1, days+1):

    if day_number % 11 == 0:
        quantity += 2

    if day_number % 2 == 0:
        budget += ornaments_price * quantity
        totalSpirit += 5
    if day_number % 3 == 0:
        budget += (tree_skirt * quantity) + (tree_garlands * quantity)
        totalSpirit += 13
    if day_number % 5 == 0:
        budget += tree_lights * quantity
        totalSpirit += 17
        if day_number % 3 == 0:
            totalSpirit += 30
    if day_number % 10 == 0:
        totalSpirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights


if days % 10 == 0:
    totalSpirit -= 30


print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
