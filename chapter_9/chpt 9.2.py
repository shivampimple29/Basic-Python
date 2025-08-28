#Q2:
# Compile Time Polymorphism (Method Overloading)
# In Python, we simulate method overloading using default arguments
class CompileTimeExample:
    def add(self, a, b, c=0): # Default value of c allows overloading
        return a + b + c
# Creating an object of CompileTimeExample
obj = CompileTimeExample()
# Calling the method with 2 arguments
print("Add 2 numbers:", obj.add(5, 10))
# Calling the method with 3 arguments
print("Add 3 numbers:", obj.add(5, 10, 15))
# Runtime Polymorphism (Method Overriding)
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
# Creating objects of Dog and Cat
animal=Animal()
dog = Dog()
cat = Cat()
# Demonstrating runtime polymorphism
animal.sound()
dog.sound() # Runtime Polymorphism - Dog's sound method is called
cat.sound() # Runtime Polymorphism - Cat's sound method is called
