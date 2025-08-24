usrname=input("Enter your username: ")
length=len(usrname)
if(length<10):
    print("username contains less than 10 chars.")
elif(length==10):
    print("username contains 10 chars.")
else:
    print("username contains more than 10 chars.")