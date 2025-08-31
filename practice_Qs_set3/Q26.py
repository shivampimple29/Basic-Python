#Q26:Write a class with a static variable college_name, and instance variables name and roll_no, and display all. 

class Student:
    college_name = "SFIT College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"College: {Student.college_name}")

s1 = Student("Radha", 1015)
s2 = Student("Shivam", 1036)

s1.display()
print()# Just for spacing:)
s2.display()
print("------------------------------------------------------")