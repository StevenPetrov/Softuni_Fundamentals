d = {'shards': 0, 'fragments': 0, 'motes': 0}
condition = False
test_word = 'shards, fragments, motes'
junk = {}

while True:
    line = input().lower().split()
    for x in range(0, len(line), 2):
        key = line[x + 1]
        value = int(line[x])
        if key in test_word:
            d[key] += value
        else:
            if key in junk:
                junk[key] += value
            else:
                junk[key] = value
        for y in d:
            if d[y] >= 250:
                condition = True
                break
        if condition:
            break
    if condition:
        break

for x in d:
    if x == 'shards' and d[x] >= 250:
        print('Shadowmourne obtained!')
        d[x] -= 250
        break
    elif x == 'fragments' and d[x] >= 250:
        print('Valanyr obtained!')
        d[x] -= 250
        break
    elif x == 'motes' and d[x] >= 250:
        print('Dragonwrath obtained!')
        d[x] -= 250
        break

for key, values in d.items():
    print(f'{key}: {values}')
for key, values in junk.items():
    print(f'{key}: {values}')
