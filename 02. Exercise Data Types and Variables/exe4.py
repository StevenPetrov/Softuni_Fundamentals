counter = int(input())
sum = 0
for x in range(counter):
    letter = input()
    sum += ord(letter)

print(f"The sum equals: {sum}")