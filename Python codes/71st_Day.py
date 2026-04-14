# - Hierarchical Inheritance
class Parent:
    def func1(self):
        print("Parent function")

class Child1(Parent):
    def func2(self):
        print("Child 1 function")

class Child2(Parent):
    def func3(self):
        print("Child 2 function")