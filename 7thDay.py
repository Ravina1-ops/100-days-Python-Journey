# Taking input from user 
# every input consider as string 
# /to perform arithmetic operation typecaste that one 

a = input("Enter your name: ")
print("My name is : ",a)

x = input("Enter first number: ")
y = input("Enter second number: ")

print( x + y ) # give xy not mathematical operation answer 

print( int(x) + int(y)) # typecasting is done to add them 

''' calculator using user input'''

b = input("Enter first number = ")
d = input("Enter second number = ")
c = int(b) + int(d)
k = int(b) - int(d)
e = int(b) * int(d)
f = int(b) / int(d)
g = int(b) // int(d)
h = int(b) % int(d)
i = int(b) ** int(d)
print("Addition of ",b,"and",d,"is = ",c)
print("Subtraction of ",b,"and",d,"is = ",k)
print("Multiplication of ",b,"and",d,"is = ",e)
print("Division of ",b,"and",d,"is = ",f)
print("Floor Division of ",b,"and",d,"is = ",g)
print("Modulus of ",b,"and",d,"is = ",h)
print(d, "raise to ",b ,"is = ",i)