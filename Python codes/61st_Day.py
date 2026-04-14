# - Alternative Constructors
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        name, salary = string.split("-")
        return cls(name, int(salary))

e1 = Employee("Harry", 12000)
e2 = Employee.fromStr("Rohan-15000") # Data parsing logic
print(e2.name, e2.salary)