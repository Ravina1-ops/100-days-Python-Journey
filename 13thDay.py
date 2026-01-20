# For Loop

x = ["Red","Blue"]
for color in x:
    print(color,end="\n")
    for i in color:
        print(i,end=",")

'''here a list is given iterate for loop for printing all 
strings of list and then iterate anpther for loop for 
printing all elements of string  '''
       

for n in range(2,22,2): 
    print(n)

'''range is used to give values from where start 
then where to step and how much difference should be kept in 
between the printing Remember always 1 to n-1 is printed not 1 to n '''

# Print Your Name And if your name consist any vowel then print the  vowels 

n = (input("Enter Your Name: ").lower())

for vowel in n:
    if vowel in "aeiou":
        print(f"'{vowel}' Vowel in your name")
        
'''The Old, Messy Way: print("Hello " + name + ", you are " + str(age) + " years old.")

The New "Boss" Way (f-string): print(f"Hello {name}, you are {age} years old.")'''


