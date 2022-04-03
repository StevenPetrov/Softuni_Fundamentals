encrypted_text = input()

while True:
    command = input()
    if command == 'Decode':
        break
    command = command.split('|')
    action = command[0]

    if action == 'Move':
        slice_word = encrypted_text[:int(command[1])]
        encrypted_text = encrypted_text[int(command[1]):] + slice_word

    elif action == 'Insert':
        value = command[2]
        index = int(command[1])
        encrypted_text = encrypted_text[:index] + value + encrypted_text[index:]

    elif action == 'ChangeAll':
        # l = list(encrypted_text)
        letter = command[1]
        new_letter = command[2]
        encrypted_text = encrypted_text.replace(letter, new_letter)
        # counter = -1
        # for x in l:
        #     counter +=1
        #     if x == letter:
        #         l[counter] = new_letter
        # encrypted_text = ''.join(l)




print(f'The decrypted message is: {encrypted_text}')