# Variables to be inserted into the string
country = "India"
name = "Ravina"

# Using placeholders {} and the .format() method
letter = "Hey my name is {} and I am from {}"
print(letter.format(name, country)) 

# You can also use index numbers to ensure variables go to the right place
# This is useful if the order in .format() changes
letter2 = "Hey my name is {1} and I am from {0}"
print(letter2.format(country, name))
 # Output: Hey my name is Ravina and I am from India


# f-strings allow direct placement of variables inside the string
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999

# Using :.2f inside the braces formats the number to 2 decimal places
txt = f"For only {price:.2f} dollars!"
print(txt) # Output: For only 49.10 dollars!

# f-strings can evaluate expressions inside the braces
print(f"{2 * 30}") # Output: 60



# To show literal curly braces in an f-string, you must double them
print(f"We use f-strings like this: Hey my name is {{name}}") 
# Output: We use f-strings like this: Hey my name is {name}