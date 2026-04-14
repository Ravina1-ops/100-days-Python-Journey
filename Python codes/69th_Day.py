#  - Multiple Inheritance
class Employee:
    def __init__(self, name):
        self.name = name

class Dancer:
    def __init__(self, dance):
        self.dance = dance

class DancingEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance)

o = DancingEmployee("Shivani", "Kathak")
print(o.name)
print(o.dance)