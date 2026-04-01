# Constructors in class

class data:
    def __init__(self,n,a):
        # constructor initialization 
        # parameterised constructor as n and a passes as parameters
        # __init__(self) is default constructor

        print("HI EVERYONE MY NAME IS ")
        # print st. run everytime when object of this class is called
        self.name = n
        self.age = a
        # methods create to assign the parameter 
    def info(self):
        print(f"{self.name} of age {self.age}")
a = data("Ravina",20)
a.info()
b = data ("naksh", 12)
b.info()