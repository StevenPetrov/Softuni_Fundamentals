budget = float(input())
price_kg_flour = float(input())
eggs_price = price_kg_flour * 0.75
milk_price = (price_kg_flour * 1.25) /4

eggs_count = 0
milk_count = 0
flour_count = 0

number_colored_eggs = 0
current_bread_count = 0
budget_left = budget

while True:
    if eggs_count == 0:
        if budget_left >= eggs_price:
            budget_left -= eggs_price
            eggs_count += 1
        else:
            break
    if milk_count == 0:
        if budget_left >= milk_price:
            budget_left -= milk_price
            milk_count += 1
        else:
            break
    if flour_count == 0:
        if budget_left >= price_kg_flour:
            budget_left -= price_kg_flour
            flour_count += 1
        else:
            break

    eggs_count -= 1
    milk_count -= 1
    flour_count -= 1

    current_bread_count += 1
    number_colored_eggs += 3
    if current_bread_count % 3 == 0:
        number_colored_eggs -= (current_bread_count - 2)

if eggs_count >= 1:
    budget_left += eggs_count*eggs_price
if milk_count >= 1:
    budget_left += milk_count * milk_price
if flour_count >= 1:
    budget_left += flour_count*price_kg_flour

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {number_colored_eggs} eggs and {budget_left:.2f}BGN left.")
