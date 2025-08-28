#Q2:Write a Python program that prompts the user to input an integer
#and raises a ValueError exception if the input is not a valid integer.
def get_num():
    try:
        n=input("Enter a number:")
        n=int(n)
        print(f"The entered integer is:{n}")
    except ValueError:
        print("Entered number is not an Integer!")
get_num()