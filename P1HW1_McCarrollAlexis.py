# Alexis McCarroll
# 9/24/2024
# P1HW1
# Get interger input froom user and perform math calculations

# Display output to the user
print("-----Calculating Exponents-----")
print()
print()

# Get information from the user
base_value = int(input("Enter an interger as the base value: "))
exponent = int(input("Enter an interger as the exponent: "))
print()
print()

# Calculate the value of the exponent math
result = base_value ** exponent

# Display the results of the math
print(base_value, "raised to the power of", exponent, "is", result, "!!")
print()
print()

print("-----Addition and Subtraction-----")
print()
print()

# Get more info from the user
starting_int = int(input("Enter a starting interger: "))
adding_int = int(input("Enter an interger to add: "))
subtract_int = int(input("Enter an interger to subtract: "))
print()
print()

# Calculate the math'
result2 = starting_int + adding_int - subtract_int

# Display result2
print(starting_int, "+", adding_int, "-", subtract_int, "is equal to", result2)
