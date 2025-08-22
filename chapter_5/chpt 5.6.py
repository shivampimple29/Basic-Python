# Q. Create an empty dictionary Allow 4 enter their favourite language as use keys as their names nomes are unique friends to values and 
# Assume that the names are unique.
dict={}
name1=input("Enter your name : ")
lang1=input("Enter a language: ")
dict.update({name1:lang1})
name2=input("Enter your name : ")
lang2=input("Enter a language: ")
dict.update({name2:lang2})
name3=input("Enter your name : ")
lang3=input("Enter a language: ")
dict.update({name3:lang3})
name4=input("Enter your name : ")
lang4=input("Enter a language: ")
dict.update({name4:lang4})
print(dict.items())

