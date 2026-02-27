#  List are ordered collection of data items.

l = [5,2,6]
print(l)

# we can print the list element one by one 

print(l[0])
print(l[2])

# A list can store int string float boolean in one 

p = ["Ravina", 8.4, "No. ", 1, True ]
print(p)

# concept of negative index is same as string l[-3] means length of list - given index of list

marks = [45,8,78,65]
print(marks[-2])
print(marks[len(marks)-2]) 
# both gives same result

'''Check whether an item is present in the list by following method'''

if "Ravina" in p:
    print("yes")
else:
    print("No") 

# it will give yes but i change ravina to ravi is give no as it is not in list but ravi is a substring of ravina so can we 
# check it also yes 

if "Ravi" in "Ravina":
    print("Yes")
else:
    print("No")

'''Concept of string slicing also applicable here in list we can print in between the indexes
one another concept is jump index which is writen after range of indexex we want to print
it give gap to print the index of that much indexes the no we have give'''

m = [2,5,8,7,4,5,6,9,3,2,1,4,5,7,8,5,6]
print(m[1:-2])
print(m[1:-1:2])
# above means start from index 1 upto index -1 which is 16 after calculation and give a jump of 2 index 

# list comprehension 

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)