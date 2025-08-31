#Q20:Write a function that returns the sum and average of a list. 

def sum_avg(a,b):
    Sum=a+b
    avg=Sum/2
    return(Sum,avg)

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
Sum,avg=sum_avg(a,b)#most imp line in the code
print(f"Sum and average of {a} and {b}:{Sum} and {avg}")
print("------------------------------------------------------