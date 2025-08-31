#Q15:Accept a character from the user and determine whether it’s a vowel or consonant. 

char=input("Enter a character:")
char=char.lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char<='a' and char>='z':
    print(f"{char} is a consonent")
else:
    print(f"{char} is not an alphabetical character")
print("--------------------OR--------------------------")
char=input("Enter a character:")
if char.isalpha()==True:
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonent")
else:
    print(f"{char} is not an alphabetical character")
print("----------------------------------------------")