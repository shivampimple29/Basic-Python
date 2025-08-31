#Q25:Extend the Student class to include a method that checks whether the student has passed (marks > 40). 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def has_passed(self):
        if self.marks > 40:
            print("Status: Passed")
        else:
            print("Status: Failed")
# Example usage
s1 = Student("Radha", 18, 100)
s1.display()
s1.has_passed()
print()# Just for spacing:)
s2 = Student("somebody", 18, 35)
s2.display()
s2.has_passed()
print("------------------------------------------------------")