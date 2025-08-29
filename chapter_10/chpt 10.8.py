#Q9:Write a Python program to get the file size of a plain file.
import os
file1 = os.stat('python.txt')
print("Size of file :", file1.st_size, "bytes")
print("-----------------------------------------------------")