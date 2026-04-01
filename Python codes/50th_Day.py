# Classes and objects
class Data:
    name = "Ravina"
    occupation = "Student"
    def info(self):
        print(f"HI I'm {self.name} and i am a {self.occupation}")
a = Data()
a.info()
a.name = "Naksh"
a.info()
a.occupation = "Brother"
print(f"Hi i am {a.name} and i am {a.occupation}")