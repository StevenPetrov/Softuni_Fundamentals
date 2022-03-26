max_star = int(input())
number = 0

while True:
    if number <= max_star:
        print(number*'*')
        number +=1
        if number == max_star:
            break

while number > 0:
        print(number*'*')
        number -=1
