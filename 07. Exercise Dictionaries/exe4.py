def phone_check():
    phonebook = {}

    while True:
        command = input()
        if '-' not in command:
            break
        command = command.split('-')
        name = command[0]
        number = command[1]
        phonebook[name] = number

    for x in range(int(command)):
        name_req = input()
        if name_req in phonebook:
            print(f'{name_req} -> {phonebook[name_req]}')
        else:
            print(f'Contact {name_req} does not exist.')


phone_check()