#Q16:Write a program to print all factors of a number entered by the user. 

num=int(input("Enter a number:"))
print(f"Factor(s) of {num} is/are:")
for i in range (1,num+1):
    if num%i==0:
        print(i)
print("----------------------------------------------")