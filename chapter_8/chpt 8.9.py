#Q2:WAP to find a^b for the given a and b using recursion.
def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return(base*power(base,exp-1))
#main Function:
base=int(input("enter the base:"))
exp=int(input("enter the exponent:"))
ans=power(base,exp)
print(f"Answer is:{ans}")