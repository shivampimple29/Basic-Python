#Q1:
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
# Single Inheritance: Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")
# Multilevel Inheritance: Cat -> Dog -> Animal
class Cat(Dog): # Dog is inherited here, creating a chain
    def meow(self):
        print(f"{self.name} meows")
# Hierarchical Inheritance: Both Dog and Tiger inherit from Animal
class Tiger(Animal): # Inheriting from Animal
    def roar(self):
        print(f"{self.name} roars")
#Multiple Inheritance: HybridDog inherits from both Tiger & cat
# Hybrid Inheritance: Combination of multiple inheritance types
class HybridDog(Tiger, Cat): # Inheriting from both Tiger and Cat
    pass
# Testing the code
print("Single Inheritance:")
dog = Dog("Buddy")
dog.speak() # Inherited method
dog.bark() # Method from Dog
print("\nMultilevel Inheritance:")
cat = Cat("Kitty")
cat.speak() # Inherited from Animal
cat.bark() # Method from Dog
cat.meow() # Method from Cat
print("\nHierarchical Inheritance:")
tiger = Tiger("Sheru")
tiger.speak() # Inherited from Animal
tiger.roar() # Method from Tiger

print("\nHybrid Inheritance:")
hybrid_dog = HybridDog("Hybrid")
hybrid_dog.speak() # Inherited from Animal
hybrid_dog.bark() # Inherited from Dog
hybrid_dog.roar() # Inherited from Tiger
print("-------------------------------------------------------")