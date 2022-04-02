while True:
    command = input()
    if command == 'end': break
    word = reversed(command)
    word = (''.join(word))
    print(f'{command} = {word}')
