#Q14:Write a program to check if a number is divisible by both 3 and 5.

num=int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible both 3 and 5.")
print("----------------------------------------------")