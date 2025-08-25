# Write a program to greet all the person name stored in a list l1 and which starts with 'S'
l1=["Athang","Shivam","Shreyash","Rahul"]
for name in l1:
    if (name.startswith("S")):
        print(f"Hello {name}")