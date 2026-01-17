# String methods 
a = "Harry"
print(len(a))  # Output: 5
print(a.upper())  # Output: "HARRY"
print(a.lower())  # Output: "harry" 

# from above we can say that string are immutable 
''' immutable means cant change that states that 
original string does not change infact a copy of that string 
is made inside and operation is performed on it '''

# rstrip: Removes trailing characters
a = "Harry!!!"
print(a.rstrip("!"))  # Output: "Harry"

# replace: Replaces all occurrences of a substring
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))  # Output: "Silver Moon"

# split: Splits string into a list based on a separator
str3 = "Harry Blog Code"
print(str3.split(" "))  # Output: ['Harry', 'Blog', 'Code']

# capitalize: First character to upper, rest to lower
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())  # Output: "Introduction to js"

# center: Aligns string to center with padding
str1 = "Welcome to the Console!!!"
print(str1.center(50)) 

# count: Returns number of occurrences
print(str1.count("Harry"))

# find: Returns index of first occurrence (returns -1 if not found)
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))  # Output: 10

# index: Same as find, but raises ValueError if not found
# print(str1.index("ishh")) # This will throw an error

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  # True if Alpha-numeric (A-Z, a-z, 0-9)
print(str1.isalpha())  # True if only Alpha (A-Z, a-z)
print(str1.islower())  # True if all characters are lowercase
print(str1.isprintable()) # True if all characters are printable (e.g., no \n)
print(str1.isspace())  # True if string contains only white spaces
print(str1.istitle())  # True if string is in title case
print(str1.isupper())  # True if all characters are uppercase

# starts-with / ends-with
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python")) # True
print(str1.endswith("!!!"))      # False

# swapcase: Swaps Upper to Lower and vice-versa
str2 = "Python Is A Language"
print(str2.swapcase()) 

# title: Converts string to title case
str1 = "his name is dan"
print(str1.title()) # Output: "His Name Is Dan"