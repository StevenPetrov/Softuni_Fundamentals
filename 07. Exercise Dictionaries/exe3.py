countries = input().split(', ')
capitals = input().split(', ')

d = dict(zip(countries,capitals))

for key,values in d.items():
    print(f'{key} -> {values}')