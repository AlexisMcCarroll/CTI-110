# Alexis McCarroll
# 11/8/2024
# P4LAB2
# Use while loop and for loop together

'''
Get integer from user
determine if integer is positive or negative
if number is positive, display multiplixation table
if number is negative, tell user program cannot accept it
ask use to run again?
if yes, run program
if no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #Display multiplication for that value from range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")
    
#Loop has broken, user entered 'no'
print("Program is ending...")
