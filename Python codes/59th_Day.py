# instances and class variable

class Employee:
    def __init__(self, name):
        self.name = name
    def showDetails(self):
        print("The name of the Employee is {self.name}")

emp1 = Employee
