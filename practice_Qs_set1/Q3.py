#Q3:Create a program that takes the principal, rate, and time from the user and calculates simple interest. 

P=int(input("Enter principal amount:"))
R=int(input("Enter Rate of Intrest :"))
T=int(input("Enter time in years   :"))
print(f"Simple Interest={(P*R*T)/100}")
print("----------------------------------------------")