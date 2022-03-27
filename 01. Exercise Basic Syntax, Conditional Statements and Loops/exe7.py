divisor = int(input())
boundary = int(input())

number = boundary

while True:
    if number > 0 and number % divisor == 0 and number <= boundary:
        print(number)
        break
    else:
        number -= 1
        continue