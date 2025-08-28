#Q1:Write a Python program to handle a ZeroDivisionError
#exception when dividing a number  by zero.
try:
    n=int(input("Enter a number:"))
    result=5/n
except ZeroDivisionError:
    print("We cannot devide any number by zero!")