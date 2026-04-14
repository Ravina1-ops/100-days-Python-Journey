#  - Magic Methods
class Employee:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"Employee name is {self.name}"

e = Employee("Harry")
print(e) # Calls __str__
print(len(e)) # Calls __len__