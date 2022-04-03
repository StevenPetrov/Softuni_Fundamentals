heroes_data = dict()
number_of_heroes = int(input())
# adding heroes
for x in range(number_of_heroes):
    hero = input().split()
    hero_name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])
    heroes_data[hero_name] = {'HP': hp, 'MP': mp}

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' - ')
    action = command[0]

    if action == 'CastSpell':
        name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_data[name]['MP'] >= mp_needed:
            heroes_data[name]['MP'] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes_data[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    if action == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes_data[name]['HP'] -= damage

        if heroes_data[name]['HP'] <= 0:
            print(f"{name} has been killed by {attacker}!")
            heroes_data.pop(name)
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_data[name]['HP']} HP left!")

    if action == 'Recharge':
        name = command[1]
        amount = int(command[2])

        heroes_data[name]['MP'] += amount
        if heroes_data[name]['MP'] <= 200:
            print(f"{name} recharged for {amount} MP!")
            # print(f"current mana {heroes_data[name]['mp']}")
        else:
            amount = abs(heroes_data[name]['MP'] - 200 - amount)
            heroes_data[name]['MP'] = 200
            print(f"{name} recharged for {amount} MP!")
            # print(f"current mana {heroes_data[name]['mp']}")
    if action == 'Heal':
        name = command[1]
        amount = int(command[2])

        heroes_data[name]['HP'] += amount
        if heroes_data[name]['HP'] <= 100:
            print(f"{name} healed for {amount} HP!")
            # print(f"current mana {heroes_data[name]['mp']}")
        else:
            amount = abs(heroes_data[name]['HP'] - 100 - amount)
            heroes_data[name]['HP'] = 100
            print(f"{name} healed for {amount} HP!")

# for keys, values in heroes_data.items():
#     print(keys)
#     for x, y in values.items():
#         print(f'  {x}: {y}')

for x in heroes_data:
    print(x)
    print(f"  HP:{heroes_data[x]['HP']}")
    print(f"  MP:{heroes_data[x]['MP']}")