# Alexis McCarroll
# 11/12/2024
# P4HW1
# Edit and ehance exiting programs

#Get number of grades
numgrades = int(input("How many scores do you want to enter? "))

#empty list to hold responses
grades = []

#loop to get the grades
for grade in range(numgrades):
    thisgrade = float(input(f"Enter score #{grade + 1}: "))
    #loop to ensure thisgrade is valid
    while thisgrade < 0 or thisgrade > 100:
        print(f"[thisgrade] INVALID Score entered!!!!")
        thisgrade = float(input(f"Enter grade #{grade + 1} again: "))
    #add the valid grades to the cart
    grades.append (thisgrade)

#Loop to print each grade in list
print()
print("--------------Results-------------")
# get the lowest score
print(f"{'Lowest Grade: ':<15}{min(grades):.1f}")
#modify the list
grades.remove (min(grades))
print(f"{'Modified List: ':<15}{(grades)}")
#get the average
average = sum(grades)/len(grades)
print(f"{'Scores Average: ':<15}{(average):.2f}")

# Determine letter grade based off the average
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade =  "B"
elif average >= 70:
    letter_grade =  "C"
elif average >= 60:
    letter_grade =  "D"
elif average <= 59:
    letter_grade =  "F"

print(f"{'Grade: ':<15}{letter_grade}")
print("-" *35)
