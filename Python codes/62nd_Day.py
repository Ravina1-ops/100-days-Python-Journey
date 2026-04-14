#  - dir, __dict__, help
x = [1, 2, 3]
print(dir(x)) # Lists all methods of a list

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.__dict__) # Returns dictionary of instance variables
# help(Person) # Returns documentation of the class