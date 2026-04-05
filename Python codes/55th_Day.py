# inheritance in python

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f" The name of student is {self.name} and id is {self.id}")

class faculty(student):
    # def __init__(self,salary):
    #     self.salary = salary
    # def showsalary(self):
    #     print(f"The salary of faculty for the student is {self.salary}")
    def showlang(self):
        print("python")

s = student("Ravina", 523)
s.showDetails()
# if i write s.showsalary here show an error 


d = faculty( "Ravina", 25)
d.showDetails()
d.showlang()