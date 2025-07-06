menu = {
    "yam": 50.00,
    "fufu": 60.00,
    "rice": 80.00,
    "pizza": 100.00,
    "meat": 200.00,
    "chicken": 200.00,
    "fish": 65.00,
}

cart = []
total = 0

print("..............MENU..............")
for key, value in menu.items():
    print(f"{key.capitalize():10}: ₦{value:.2f}")
print("............................")

while True:
    food = input("Select from the menu (type 'q' to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"{food.capitalize()} added to cart.")
    else:
        print("Item not on the menu. Please try again.")

print("\nItems in your cart:", ", ".join(cart))

for food in cart:
    total += menu[food]

print(f"Total amount: ₦{total:.2f}")
