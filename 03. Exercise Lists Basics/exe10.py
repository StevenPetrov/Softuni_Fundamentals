energy = 100
coins = 100

actions = input().split('|')
condition = False
for x in actions:
    action = x.split('-')
    action[1] = int(action[1])
    if action[0] == 'rest':
        if energy + action[1] > 100:
            print(f"You gained {100-energy} energy.")
            energy = 100
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {action[1]} energy.")
            energy += action[1]
            print(f"Current energy: {energy}.")
    elif action[0] == "order":
        if energy >= 30:
            print(f"You earned {action[1]} coins.")
            coins += action[1]
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins >= action[1]:
            print(f"You bought {action[0]}.")
            coins -= action[1]
        else:
            print(f"Closed! Cannot afford {action[0]}.")
            condition = True
            break

if not condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
