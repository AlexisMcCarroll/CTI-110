# This program simulates shopping and displaying recipts

# Get info from item one
item1 = input("Enter first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))
print()

# Get info for item two
item2 = input("Enter second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))
print()

# Get info for item three
item3 = input("Enter third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))
print()

# Display the top of the recipt
print("Thanks for shopping at Harris Teeter!")
print("-" *80)
print()
item = "ITEM"
quantity = "QUANTITY"
item_total = "ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{item_total}")
print()
print(f"{item1:<20}{quantity1:<15}${price1 * quantity1:.2f}\n")
print(f"{item2:<20}{quantity2:<15}${price2 * quantity2:.2f}\n")
print(f"{item3:<20}{quantity3:<15}${price3 * quantity3:.2f}\n")
print()

# Calculate subtotal
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
print(f"Subtotal: ${subtotal:.2f}\n")

# Calculate the tax

tax = subtotal * 0.07
print(f"Tax owed: ${tax:.2f}\n")

# Calculate the total
total = subtotal + tax
print(f"Total: ${total:.2f}")
