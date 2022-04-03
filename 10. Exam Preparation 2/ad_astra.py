import re

text = input()

pattern = r'#[a-zA-Z ]+#[0-9]{2}/[0-9]{2}/[0-9]{2}#[0-9]+#|\|[a-zA-Z ]+\|[0-9]{2}/[0-9]{2}/[0-9]{2}\|[0-9]+\|'

filter_pattern = r'[\|#](?P<name>[A-Za-z ]+)[\|#](?P<date>\d+/\d+/\d+)[\|#](?P<cal>\d+)[\|#]'

n = re.findall(pattern,text)

cal_count = []

for x in n:
    delta = re.finditer(filter_pattern, x)
    for y in delta:
        cal_count.append(int(y['cal']))

final_cals = sum(cal_count) // 2000
print(f'You have food to last you for: {final_cals} days!')

for x in n:
    delta = re.finditer(filter_pattern, x)
    for z in delta:
        print(f"Item: {z['name']}, Best before: {z['date']}, Nutrition: {z['cal']}")