#Q27: Create a base class Animal with a method speak(), and subclasses Dog and Cat that override speak(). 

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("The cat says: Meow!")

a = Animal()
a.speak()

d = Dog()
d.speak()

c = Cat()
c.speak()
print("------------------------------------------------------")