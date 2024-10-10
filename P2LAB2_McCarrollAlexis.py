# Alexis McCarroll
# 10/10/2024
# P2LAB2
# Using some dictionaries

# create a dictionary
cars = {"Camero" : 18.21, "Prius" : 52.36, "Model S" : 110, "Silverado" : 26}

# variable that holds only the keys from the dictionary
keys = cars.keys()

#show akk the keys to the user
print(keys)
print()

# Get a car (key) from the user
selected_car = input ("Enter a vehicle to see it's mpg: ")
print()

# display the selected car and its mpg
print(f"The {selected_car} gets {cars[selected_car]} mgp.")
print()

# get the number of miles to drive the car
miles_planned = float(input (f"How many miles will you drive the {selected_car}? "))
print()

# Calculate gallons of gas needed
gas_needed = miles_planned / cars[selected_car]
print()

# Display gallons needed to user
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {selected_car} {miles_planned} miles.")
