# Example similar to P4HW1 
# Alexis McCarroll

# List of available items (this is not needed in hw)
availableitems = ["litter", "cat food", "feather", "collar", "toy", \
                  "litter box", "flea meds", "treats"]

# get number of items to purchase
numitems = int(input("How many items will you purchase? "))

# Empty list to hold valid responses
cart = []

# Loop to get the items
for item in range(numitems):
    thisitem = input(f"Enter item #{item + 1}: ")
    # loop to ensure thisitem is in the availableItems
    while thisitem not in availableitems:
        print(f"{thisitem} is not in stock!")
        thisitem = input(f"Enter item #{item + 1} again: ")
    # add tje valid item to the cart
    cart.append (thisitem)

# Loop to print each item in the cart
print()
print("Items we purchased are: ")
for product in cart:
    print(product)