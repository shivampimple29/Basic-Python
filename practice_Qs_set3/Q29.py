#Q29: Write a Python Program that does the following task Ask the user to enter a number as an input Use math module to calculate Square root of a number. 

import math
num = float(input("Enter a number: "))
if num >= 0:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")
else:
    print("Square root of a negative number doesn't exist.")
print("------------------------------------------------------")