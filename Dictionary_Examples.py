# in class example on dictionaries

# create a dictionary
cactus = {"cactus_color": "Dark green", "price":32.98, "max_height":60, "is_perennial":True}

# get a value, given the key
print(f"${cactus['price']:.2f}")

# get another value, given the key
print(f"Is the cactus a perinnial? {cactus['is_perennial']}")

# get value
print(cactus['cactus_color'])

# add a key value pair
cactus["water_needed"] = "1 oz per day"

# print the entire dictionary
print(cactus)

# add a key value pair
cactus.update({"prickle_color":"brown", "sun_needed":6,})

print("\n \n")
# print the entire dictionary
print(cactus)

print() 
# remove something from the dictionary
del cactus['prickle_color']
print(cactus)

print()
#print all keys in dictionary
print(cactus.keys())

# ask the user to give a key in the dictionary
answer = input("Enter a key from the dictionary: ")

# give the value associated with the user's answer
print(f"The value for {answer} is {cactus[answer]}")
