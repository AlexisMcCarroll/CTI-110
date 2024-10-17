# Alexis McCarroll
# 10/17/24
# P2HW1
# This project shows how to caclulate travel expenses

print("This program calculates and displays travel expenses")
print()

# variables and input !
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
total = budget - gas - hotel - food


# calculate the travel expenses

print("*********Travel Expenses*********")
print(f"{'Location: ':<20}{destination}")
print(f"{'Inital Budget: ':<20}${budget:,.2f}")
print(f"{'Fuel: ':<20}${gas:,.2f}")
print(f"{'Accomodation: ':<20}${hotel:,.2f}")
print(f"{'Food: ':<20}${food:,.2f}")
print("+"*25)
print()
print(f"{'Remaining Balance: ':<20}${total:,.2f}")
