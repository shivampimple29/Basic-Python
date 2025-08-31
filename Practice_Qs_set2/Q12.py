#Q12:Take input of marks from the user and display the grade using if-elif-else (A, B, C, D, F). 

marks=int(input("Enter the marks:"))
if marks>=90:
    print("Grade:A")
elif 90>marks>=80:
    print("Grade:B")
elif 80>marks>=70:
    print("Grade:C")
elif 70>marks>=60:
    print("Grade:D")
elif 60>marks>=50:
    print("Grade:E")
else:
    print("Grade:F")
print("----------------------------------------------")