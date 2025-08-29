#Q4:Write a Python program to read last n lines of a file.
N = int(input("Enter N value: "))
f=open("python.txt", 'r')
lines= f.readlines()
print("The following are the last",N,"lines of a text file:")
for t in (lines[-N:]):
    print(t)
f.close