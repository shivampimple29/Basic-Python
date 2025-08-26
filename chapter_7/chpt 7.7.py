#Q4:WAP to print prime numbers in the range given by user.
l=int(input("Enter a lower limit:"))
u=int(input("Enter a upper limit:"))
while(l<=u):
    count=0
    for i in range(2,l+1):
      if l%i==0:
            count+=1
    if count==1:
        print(l)
    l+=1