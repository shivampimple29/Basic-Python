#Q18:Write a program to check if a number is a perfect number. 

num=int(input("Enter a number:"))
sum=0
for i in range (1,num):
    if num%i==0:
        sum=sum+i
if(sum==num):
    print("Given number is a perfect number.")
else:
    print("Given number is not a perfect number.")
print("----------------------------------------------")