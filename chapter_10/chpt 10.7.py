#Q8:Write a Python program to count the number of lines in a text file.
with open("python.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)