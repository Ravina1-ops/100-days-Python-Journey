# instances and class variable

class Employee:
    company_name = "Apple" # CLASS VARIABLE (Shared by all)
    no_of_employees = 0    # Shared counter

    def __init__(self, name):
        self.name = name   # INSTANCE VARIABLE (Unique to each)
        self.raise_amount = 0.02
        Employee.no_of_employees += 1 # Update shared class variable

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in in {self.company_name} is {self.raise_amount}")

# --- TESTING ---
emp1 = Employee("Harry")
emp1.raise_amount = 0.3 # Changes ONLY for emp1
emp1.company_name = "Apple India" # Creates an instance variable for emp1, doesn't change Apple globally
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails() # Still shows "Apple" because company_name is shared