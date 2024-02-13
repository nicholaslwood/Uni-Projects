# This program calculates the daily pay for an Uber driver in New York City

# Constants 
HOURLY_RATE = 15.50 # The hourly rate for the driver in New York
COMMISSION_RATE = 0.05 # The commission rate 

# User Input 
miles_driven = float(input("Enter the number of miles driven for the day: "))
hours_worked = float(input("Enter the number of hours worked for the day: "))
tips_received = float(input("Enter the amount of tips reveived for the day: "))

# Calculations 
daily_wage = hours_worked * HOURLY_RATE
commission_pay = miles_driven * COMMISSION_RATE
total_pay = daily_wage + commission_pay + tips_received

# Output 
print("Daily wage: \$" , daily_wage)
print("Commission pay: \$" , commission_pay)
print("Tips: \$" , tips_received)
print("Total pay for the day: \$" , total_pay)


