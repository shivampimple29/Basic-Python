def pattern(n):
    for i in range(n,0,-1):
        print('*'*i)

n=int(input('Enter :'))
print(pattern(n))

print('-------------------------')

def patt(n1):
    if n1==0:
        return
    print('*'*n1)
    patt(n1-1)

patt(3)