lost_fights = int(input())

helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

expenses = 0
shield_broken_counter = 0

for x in range(1, lost_fights+1):
    if x % 2 == 0:
        expenses += helmet
    if x % 3 == 0:
        expenses += sword
        if x % 2 == 0:
            expenses += shield
            shield_broken_counter +=1
            if shield_broken_counter % 2 == 0:
                expenses += armor

print(f"Gladiator expenses: {expenses:.2f} aureus")
