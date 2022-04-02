word = input()
test = []
clean = []

for x in word:
    test.append(x)

counter = 0
for x in test:
    counter += 1
    if counter == len(test):
        clean.append(x)
    elif x != test[counter]:
        clean.append(x)

print(''.join(clean))