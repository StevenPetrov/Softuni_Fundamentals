text = input()
emoji_l = []
counter = 0
for x in text:
    counter += 1
    if x == ':':
        dlg = text[counter]
        if dlg != ' ':
            emoji = x + dlg
            emoji_l.append(emoji)

for x in emoji_l:
    print(''.join(x))
