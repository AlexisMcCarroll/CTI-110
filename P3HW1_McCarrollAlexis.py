# Alexis McCarroll
# 10/17/24
# P2HW2
# Understanding of lists


#ask the user to enter grades from tests
mod1 = float(input(f"Enter grade for Module 1: "))
mod2 = float(input(f"Enter grade for Module 2: "))
mod3 = float(input(f"Enter grade for Module 3: "))
mod4 = float(input(f"Enter grade for Module 4: "))
mod5 = float(input(f"Enter grade for Module 5: "))
mod6 = float(input(f"Enter grade for Module 6: "))

#create a list with values in it
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

print()
print("---------Results---------")

#get the lowest grade
print(f"{'Lowest Grade: ':<15}{min(grades)}")

#get the highest grade
print(f"{'Highest Grade: ':<15}{max(grades)}")

#get the sum of the grades
print(f"{'Sum of Grades: ':<15}{sum(grades)}")

#get the average of the grades
average = sum(grades)/len(grades)

#give the average of the grades
print(f"{'Average:':<15}{average:.2f}")
print("-------------------------")




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

#Display the grade and average
print(f"Average: {average}        Letter Grade: {letter_grade}")
