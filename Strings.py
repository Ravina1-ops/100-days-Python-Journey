# In python anything that you enclosed between single or double quotation marks is considered as string. ""
name = "ravina"
print(name)
print("hii", name)
apple = 'he said , "I want to eat an apple'
print(apple)
# for multiple line string we use single cot triple times for ex 
st = '''hii ravina 
how are you 
are your python programming going good or not'''
print(st)
print(name[4])
print(name[3])
print(name[2])
print(name[1])
# print(name[8]) throws an erroe because name contains only 0 to 5 
# here 0 to 5 is an sequence order character,  for a long paragraph we use for loop as shown
for character in st:
    print(character)