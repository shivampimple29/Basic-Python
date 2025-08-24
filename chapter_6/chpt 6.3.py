#Q. A spam comment is definded as a text containing following Keywords:"make a lot of money", "buy now", "click this","subscribe now". Write a 
# program to detect these spams.
msg=input("Enter a comment: ")
s1="make a lot of money"
s2="buy now"
s3="click this"
s4="subscribe now"
if((s1 in msg) or (s2 in msg) or (s3 in msg) or (s4 in msg)):
    print("SPAM DETECTED!")
else:
    print("NOT A SPAM")