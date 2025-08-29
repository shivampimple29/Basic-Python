#Q.5 Write a Python program to read a file line by line store it into a variable.
file=open('python.txt', 'r')
# Read all the lines of the file into a list
lines = file.readlines()
print(lines)