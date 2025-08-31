#Q13:Create a program that determines if a year entered by the user is a leap year. 

year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("----------------------------------------------")