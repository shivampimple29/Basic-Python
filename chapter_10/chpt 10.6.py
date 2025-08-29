#Q6:Write a Python program to read a file line by line and store it into a list.
#Q7:Write a Python program to read a file line by line store it into an array.
array1 = []
f=open('python.txt')
for line in f:
    array1.append(line)
print(array1)