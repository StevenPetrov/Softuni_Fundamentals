year = int(input())

not_found = True

while not_found:
    list = []
    year += 1
    for x in str(year):
        list.append(x)
    if len(str(year)) == len(set(list)):
        not_found = False
        print(year)

