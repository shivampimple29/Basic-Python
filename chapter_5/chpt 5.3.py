#Q. Write a program to create a dictionary of Hindi words with values as their english translation Provide user with an option to look it up!
d={"chashma":"spectacles",
  "billi"   :"cat" ,
  "suraj"   :"sun"}
word=input("Enter required word:")
print(d.get(word))