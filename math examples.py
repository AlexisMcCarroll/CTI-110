# In class examples of math equations

# Import random library for use in the program
import random

'''
# Get value of the sides from the user
side1 = float(input("Enter values for side 1: "))
side2 = float(input("Enter values for side 2: "))
'''

# Generate random values for side 1 and side 2
side1 = random.randint(2,7)
side2 = random.randint(2,7)

# Calculate the hypotenuse
hypotenuse = (side1 ** 2) + (side2 ** 2)

# Display the results to the user
print(f"The hypotenuse of a right triangle with the sides {side1} and {side2} is {hypotenuse}")