#Q2:WAP to print first n prime numbers where n is given by user.
n=int(input("Enter a number: "))  
k=2  
while k<=n:  
    count=0 
    for i in range(2,k+1):  
        if k%i==0:
            count+=1
    if count==1:  
        print(k)
    k+=1 