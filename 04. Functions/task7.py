def rounding(llist):
    new_list = []
    llist = list(map(float, llist.split()))
    for x in llist:
        new_list.append(round(x))
    return new_list


print(rounding(input()))
