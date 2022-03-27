counter = int(input())

for x in range(97, 97+counter):
    for y in range(97, 97+counter):
        for z in range(97, 97+counter):
            print(chr(x)+chr(y)+chr(z))
