#Q24:Define a class Student with instance variables for name, age, and marks. Include a method to display them. 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Marks: {self.marks}")
        
s1 = Student("Radha", 18, 100)
s1.display()
print("------------------------------------------------------")