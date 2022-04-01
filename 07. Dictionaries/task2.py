l = input().split()
d = {}

for x in range(0, len(l), 2):
    product = l[x]
    quantity = l[x + 1]

    d[product] = int(quantity)

search = input().split()

for x in search:
    if x in d:
        print(f"We have {d[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")
