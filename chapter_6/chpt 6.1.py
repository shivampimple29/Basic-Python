#Q. Write a program to find greatest of four numbers entered by the user.
a=int(input("Enter a unique Number :"))
b=int(input("Enter a unique Number :"))
c=int(input("Enter a unique Number :"))
d=int(input("Enter a unique Number :"))
if(a>b and a>c and a>d):
    print("a is greatest number.")
elif(b>c and b>d):
    print("b is greatest number.")
elif(c>d):
    print("c is greatest number.")
else:
    print("d is greatest number.")

