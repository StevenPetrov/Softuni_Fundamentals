number_of_snowballs = int(input())

snowball_value = 0

for x in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = int((snowball_weight / snowball_time) ** snowball_quality)
    if value >= snowball_value:
        snowball_value = value
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {snowball_value} ({best_snowball_quality})")
