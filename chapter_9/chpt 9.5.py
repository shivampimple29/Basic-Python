#Q3:Write a Python program that prompts the user to input two numbers
#and raises TypeError exception if the inputs are not numerical.
def get_number():
    try:
        num1=input("Enter the first num:")
        num2=input("Enter the second num:")
        num1=float(num1)
        num2=float(num2)
        print(f"Numbers are:{num1} and {num2}")
    except ValueError:
        raise TypeError("Both inputs must be numerical.")
get_number()