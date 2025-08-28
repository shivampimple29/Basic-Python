#Q5:Write a Python program that prompts the user to input a number
#and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    n=int(input("Input a num:"))
    print("Entered number is:",n)
except KeyboardInterrupt:
    print("Input Cancelled by User.")
print("--------------------------------------------------------------------------")
