# Typecasting means convert one type of data into other 
a1 = "1" 

a = 1 

b2 = "2"

b = 2

print(a + b)

print(a1 + b2) # gives 12 as output as it consider 1 and 2 as string not integers

print(int(a1) + int(b2))

''' this int(a1) is explixit typecasting which convert and tell the interpretare that use 1 and 2 as int not str 
and perform that operation but make sure given string is a valid number'''
 
k = 5 

l = 3.6

m = k + l

print(m , type(m))

''' above give a float value due to implicit typecasting '''

num = 45

string = "90"

print(num + int(string))

# through above we can add 45 and 90 as integers easily
