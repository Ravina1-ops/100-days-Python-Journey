# decorators in python = basically used for modifying a function taking that as an argument

def greet(fx):
    def mfx():
         print("According to question statement")
         fx()
         print("Here we solved the question")
    return mfx

# here by using @greet decorator we modify the function math and mul by adding two statements in both 

@greet
def math():
    x = 7
    y = 9
    print(f"x = {x} and y = {y} Add = {x+y}")


def mul():
    a = 5
    b = 4
    print(f"x = {a} and y = {b} multiply = {a*b}")


math()
greet(mul)()
# 2nd method of decorators calling