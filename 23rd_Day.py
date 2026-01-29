# Operation on tuple 

tuple1 = (0,1,2,3,2,3,2,3,2,3,1,0)

r = tuple1.count(3)
p = tuple1.index(3)
o = tuple1.index(3,2,6)
# element starting index then ending index 
l = len(tuple1)


print("length of 3 in tuple1 is: ",l)
print("Count of 3 in tuple1 is: ",r)
print("index of 3 in tuple1 is: ",p)
print("index of 3 in tuple1 between given range: ",o)

countries =("Pakistan","Afghanistan","Bangladesh","Srilanka")
countries1 = ("Vietnam","India","China")
Countries2 = countries1 + countries
print(Countries2)

C = ("Spain","Itlay","India")
temp = list(C)
temp.append("Russia")
temp.pop(1)
temp[1] = "Finland"
C = tuple(temp)
print(C)