# Restaurant Menu Dictionary
menu = {
    "Burger": 50,
    "Pizza": 75,
    "Pasta": 60,
    "French Fries": 40,
    "Coffee": 30,
    "Juice": 25
}

# Display Menu
def show_menu():
    print("\n🍽 Welcome to Python's Bistro 🍽")
    print("Here's what we have:\n")
    for item, price in menu.items():
        print(f"{item}: ${price}")

# Take Order
def take_order():
    order = []
    total = 0
    while True:
        choice = input("\nEnter item to order (or 'done' to finish): ").title()
        if choice == "Done":
            break
        elif choice in menu:
            order.append(choice)
            total += menu[choice]
            print(f"✅ {choice} added to your order!")
        else:
            print("❌ Item not on the menu, try again.")
    return order, total

# Main Execution
show_menu()
order, total = take_order()

print("\n🛒 Your Order:")
for item in order:
    print(f"- {item} (${menu[item]})")
print(f"\n💰 Total Bill: ${total}")
print("\n🍀 Thank you for dining with us!")
