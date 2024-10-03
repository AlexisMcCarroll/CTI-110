
# Alexis McCarroll
# 9/26/2024
# P1HW2
# I will be creating a program that does some basic math on numbers that are entered.
# First, i need to gather information from the user

print ("This program calculates and displays travel expenses")
print()
budget = int(input("enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_price = int(input("How much do you think you will spend on gas? "))
print()
hotel_price = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_price = int(input("Last, how much do you need for food? "))
print()

# Now i am going to calculate everything together
print("-------Travel Expenses-------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas_price}")
print(f"Accomodation: {hotel_price}")
print(f"Food: {food_price}")
print()

total = budget - gas_price - hotel_price - food_price

print(f"Remainging Balance: {total}")
