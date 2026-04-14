# - Multilevel Inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class GoldenRetriever(Dog):
    def color(self):
        print("Golden color")

g = GoldenRetriever()
g.eat()  # From Animal
g.bark() # From Dog