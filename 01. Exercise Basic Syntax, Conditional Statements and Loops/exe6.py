number_of_orders = int(input())
total_order_price = 0
for x in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    current_order_price = price_per_capsule*days*capsule_count
    print(f"The price for the coffee is: ${current_order_price:.2f}")
    total_order_price += current_order_price

print(f"Total: ${total_order_price:.2f}")