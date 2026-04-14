#  - Super Keyword
class Parent:
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    def child_method(self):
        super().parent_method() # Calls parent logic
        print("This is child method")

c = Child()
c.child_method()