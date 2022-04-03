targets = dict()

while True:
    command = input()
    if command == 'Sail':
        break
    command = command.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city in targets:
        targets[city]['population'] += population
        targets[city]['gold'] += gold
    else:
        targets[city] = dict()
        targets[city]['population'] = population
        targets[city]['gold'] = gold

while True:
    command = input()
    if command == 'End':
        break
    command = command.split('=>')
    action = command[0]

    if action == 'Plunder':
        city = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        targets[city]['population'] -= people
        targets[city]['gold'] -= gold
        if targets[city]['population'] <= 0 or targets[city]['gold'] <= 0:
            print(f"{city} has been wiped off the map!")
            targets.pop(city)

    if action == 'Prosper':
        city = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targets[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {targets[city]['gold']} gold.")

if len(targets) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for city in targets:
        print(f"{city} -> Population: {targets[city]['population']} citizens, Gold: {targets[city]['gold']} kg")
