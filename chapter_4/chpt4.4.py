#tuple operations
tup=("Shivam",2,45,"bird")
print("first element of tup:",tup[0])
print("Number of birds are:",tup.count('bird'))
print("First occurence of 2 is at index:",tup.index(2))
a="Shivam"
b=tuple(a)
print(b)