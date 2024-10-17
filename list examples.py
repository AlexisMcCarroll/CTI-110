# in class examples using lists

# create an empty list
myfam = []

# add values to the list
myfam.append("Alexis")
myfam.append("Lisa")
myfam.append("Billy")
myfam.append("Brooklyn")
myfam.append("Max")
myfam.append("Chloe")
myfam.append("Willow")

# display list
print(myfam)

# print item at index 3
print(myfam[3])

# print items from index 1-3 (goes up to but not including 3)
# add one to your ending index
print(myfam[1:4])

print("Remove Willow...")
# remove item from list by value
myfam.remove("Willow")
print(myfam)

print("Remove Dad...")
# remove item from list by index
myfam.pop(2)
print(myfam)


num1 = int(input("gimme a number: "))
num2 = int(input("gimme a number: "))
num3 = int(input("gimme a number: "))
num4 = int(input("gimme a number: "))
num5 = int(input("gimme a number: "))
num6 = int(input("gimme a number: "))

# create the list with the values in it
numbers = [num1, num2, num3, num4]
print(numbers)


# functions that use lists

# gives back tbe number of items in the list
print(f" get the lowest items in the list {len(numbers)}")

# get the highest value in the list
print(f"the highest value in the list is {max(numbers)}")

# get the sum of all values in the list
print(f"the sum of value in the list is {sum(numbers)}")

# get avevrage
average =  sum(numbers)/len(numbers)

# display average
print(f"the average of value in the list is {average(numbers)}")

