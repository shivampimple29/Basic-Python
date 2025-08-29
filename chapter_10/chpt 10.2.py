#Q2:Write a Python program to read first n lines of a file.
def file_read(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read('python.txt',2)
print("-----------------------------------------------------")
N = int(input("Enter N value: "))
f=open("python.txt", 'r')
lines= f.readlines()
print("The following are the first",N,"lines of a text file:")
for t in (lines[:N]):
    print(t)
    f.close()