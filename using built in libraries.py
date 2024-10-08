# using python built-in libraries
# import the datetime library to use it in the program
import datetime

# assign the current date and time to a variable
time = datetime.datetime .now()
month = time.month

month_word = time.strftime("%B")

# display date/time
print(f"the current date and time is {time}")
print(f"the current month is {month}")
print(f"the current month is {month_word}")

today = datetime.datetime.today()
print(f"Today is {today}")

weekday = today.weekday()
weekday = int(weekday)

print(f"The day of the week is {weekday}")

# Gets the datatype of the variable
print(type(weekday))
print()
'''
# Get day of week from user as interger
weekday = int(input("Enter an interger 0-6 as the day of the week: "))
'''
# if-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"

elif weekday == 1:
    weekday_word = "Tuesday"

elif weekday == 2:
    weekday_word = "Wednesday"

elif weekday == 3:
    weekday_word = "Thursday"

elif weekday == 4:
    weekday_word = "Friday"

elif weekday == 5:
    weekday_word = "Saturday"

elif weekday == 6:
    weekday_word = "Sunday"

else:
    print("Invalid day of week!!!")
    weekday_word = "INVALID"


print()
print(f"The day of the week is {weekday_word}")
