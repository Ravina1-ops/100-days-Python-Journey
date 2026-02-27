# String Slicing = it means printing desired letters from a string 
 
nm = "Harry"
print("Length is ", len(nm)) # len is used to given length of string 

name = "Ravina"
print(name[0:3])
'''it is positive index slicing of string in which it gives the 
output of letter index 0 to 3-1 only RAV will print '''

print(name[:4]) 
print(name[:])

'''if we not write 0 in slicing it automatically consider 0 there
and if we dont write ending index then it will consider length as ending like 6 
in above example and it print from 0 to 6-1 ravina'''

print(name[-1:-3])
print(nm[-4:-2])

'''it is negative slicing it means len(name)-given index 
like above length is 6 and given starting is -1 and ending is -3
so it means print from 5 index to 3-1 and it does not make any sense 
so nothing will print here'''

''' in nm negatuve slicing length is 5 and given starting index is -4
and ending is -2 so it means print from index 1 to 3-1 so ar is printed in this'''

