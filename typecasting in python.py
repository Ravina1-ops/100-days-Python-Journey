# typecasting in python 
a="1"
a1="1"
a2=1
b="5"
b2="5"
b3=5
print(a+b)
print(a2+b3)
print(int(a1)+int(b2))
# The conversion of one data type into the other data type is known as type casting in python 
# python suppoerts a wide variety of functions or methods like; int(), float(), str(), ord(), tuple(), list(), dict(), for type casting in python  
# types of typecasting two: 
# 1. explicit type conversion = in which we order to covert the numbers or function for example=
string = "15"
number = 5
string_number = int(string) # throws an error if the string is not a valid integer
sum = number + string_number
print("the sum of both the numbers is: ", sum)
# output : the sum of both the number is 20 
# 2. implicit typecasting : when one data type is converted into other by the python interpreter itself. ex=
# python converts a smaller data type to a higher data type to prevent data loss 
# python automatically converts a to int 
a=7 
print(type(a))
b=3.0 
print(type(b))
c=a+b
print(type(c))
# output is int , float, float 
# python automatically coverts c to float as it is a float addition 

