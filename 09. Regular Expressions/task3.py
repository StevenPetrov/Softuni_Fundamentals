import re

years = input()
expression = r"(?P<day>\b\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

clean = re.finditer(expression, years)

for x in clean:
    day = x.group('day')
    month = x.group('month')
    year = x.group('year')

    print(f'Day: {day}, Month: {month}, Year: {year}')