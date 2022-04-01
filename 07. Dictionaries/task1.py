line = input().split()
bakery = {}

for x in range(0,len(line),2):
    product = line[x]
    value = line[x+1]
    bakery[product] = int(value)
print(bakery)
