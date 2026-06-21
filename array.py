# 1. An array of integers (temperatures in Celsius)
temperatures = [22, 25, 19, 28, 31, 24, 20]

print("=== TEMPERATURES ===")
print("Temperatures:", temperatures)
print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))
print("Average temperature:", sum(temperatures) / len(temperatures))

# 2. An array of strings (shopping list)
shopping_list = ["apples", "milk", "bread", "eggs", "coffee"]

print("\n=== SHOPPING LIST ===")
print("Items to buy:")
for item in shopping_list:
    print("-", item)

# 3. An array of booleans (user active statuses)
user_status = [True, False, True, True, False]

print("\n=== USER STATUS ===")
print("User statuses:", user_status)

active_users = user_status.count(True)
inactive_users = user_status.count(False)

print("Active users:", active_users)
print("Inactive users:", inactive_users)

# 4. An array of products in an e-commerce cart
cart = [
    {"name": "Laptop", "price": 899.99, "quantity": 1},
    {"name": "Mouse", "price": 25.50, "quantity": 2},
    {"name": "HDMI Cable", "price": 12.00, "quantity": 3},
    {"name": "Headphones", "price": 150.00, "quantity": 1}
]

print("\n=== SHOPPING CART ===")

total_cost = 0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total_cost += item_total

    print(f"Product: {item['name']}")
    print(f"  Price: ${item['price']:.2f}")
    print(f"  Quantity: {item['quantity']}")
    print(f"  Subtotal: ${item_total:.2f}")
    print()

print("Total Cart Value: $", round(total_cost, 2))