# ALexis McCarroll
# 10/29/2024
# P3HW2
# Program calculates paycheck based on OT or no OT

'''
Input: Get employee name from user - string (name)
Input: Get hours worked from user - int (hours)
Input: Get pay rate from user - float (pay_rate)

Output: print dotted line and employee name

If hours is greater than 40 (employee has OT)
    variable for hours worked already exists (don't have to create)
    (don't have to create pay rate, it already exists)
    create a variable (OT) that holds only the OT hours (hours - 40)
    create a variable for OT_pay_rate (pay_rate * 1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay (pay_rate * 40)
    Calculate gross pay (pay for OT + regular pay)
else (NO OT - hours has to be 40 or less)
       create a variable (OT) that holds only the OT hours WHICH IS ZERO
       calculate pay for OT hours WHICH IS ZERO
       calculate regular pay (pay_rate * hours)
       Calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print(f"{hours:<20}${pay_rate:<20.2f}")
       

'''

name = input(f'Enter employees name or "Done" to terminate: ')

while name.lower() != "done":
    hours = int(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    
    OT_hours = 0
    OT_payrate = pay_rate * 1.5
    OT_pay = 0 
    if hours > 40:
        OT_hours = hours - 40
        reghourpay = pay_rate * 40
        OT_pay = OT_payrate * OT_hours
    else:
        reghourpay = pay_rate * hours


    gross_pay = reghourpay + OT_pay



    print(f"Employee name: {name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("-" * 90)
    print(f"{hours:<15.1f}{pay_rate:<15}{OT_hours:<15.1f}{OT_pay:<15.2f}{reghourpay:<15.2f}{gross_pay:<15.2f}")
    print()
    name = input(f"Enter employee's name or 'Done' to terminate: ")
