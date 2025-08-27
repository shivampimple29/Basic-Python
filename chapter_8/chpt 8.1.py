def got3n(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    else:
        return n3

n1=2
n2=3
n3=4
ans=got3n(n1,n2,n3)
print(f'Greatest among the entered 3 number is {ans}')