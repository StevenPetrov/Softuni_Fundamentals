persons = int(input())
cap = int(input())

courses = 1

while persons > cap:
    persons -= cap
    courses += 1

print(courses)