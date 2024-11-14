# Examples similar to P4HW2 using loops

# While loop to control the program

# Create variables to hold totals
numitems = 0
totalcost = 0

# Variable to control the loop

product = input("Enter product name or 'exit' to terminate: ")


# Create while loop
while product.lower() != "exit":
    # increment numitems by 1
    numitems += 1
    cost = float(input(f"Enter cost for {product}: "))
    totalcost += cost
    print()
    product = input("Enter product name or 'exit' to terminate: ")
# Loop breaks here
print(f"Total number of items purchased: {numitems}")
print(f"Total cost of items purchased: ${totalcost:.2f}")
