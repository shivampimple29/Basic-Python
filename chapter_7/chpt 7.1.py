# Q: Write  a program to print multiplication table of a given number using for loop.
i=1
t=int(input("Enter a number:"))
for i in range(1,11):
    print(t*i)
    i+=1


while(i<11):
    print(t*i)
    i+=1