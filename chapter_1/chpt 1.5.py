#Q To print the contents of a directory using Python's "es' module, you can utilize the "os.listdir() function. 
# This function returns a list of all files and directories in the specified directory. Here's a simple example:
import os

directory_path = '/'  # Change this to your target directory

contents = os.listdir(directory_path) #Use the OS module to list the directory content
   
print(contents)  #Print the contents of the directory

