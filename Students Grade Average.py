# Program to find a Students Grade Average 

english = float(input("Please enter English Grade: "))
math = float(input(" Please enter Math Grade: "))
science = float(input(" Please enter Science Grade: "))
history = float(input(" Please enter History Grade: "))

total = english + math + science + history 
percentage = (total / 500) * 100

print("Total Grade = %.2f" %total)
print("Grade Percentage = %.2f" %percentage)

if(percentage >=90):
    print("A Grade")
elif(percentage >=80):
    print("B Grade")
elif(percentage >=70):
    print("C Grade")
elif(percentage >=60):
    print("D Grade")
elif(percentage >=50):
    print("F Grade")
else: 
    print("Fail")
