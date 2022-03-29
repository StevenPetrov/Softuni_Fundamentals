inventory = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == "Craft!":
        print(', '.join(inventory))
        break
    if command[0] == 'Collect':
        if command[1] in inventory:
            pass
        else:
            inventory.append(command[1])
    if command[0] == 'Drop':
        if command[1] in inventory:
            inventory.remove(command[1])
    if command[0] == 'Combine Items':
        items12 = command[1].split(':')
        if items12[0] in inventory:
            index = inventory.index(items12[0]) + 1
            inventory.insert(index, items12[1])
    if command[0] == 'Renew':
        switch_item_index = inventory.index(command[1])
        item = inventory.pop(switch_item_index)
        inventory.append(item)
