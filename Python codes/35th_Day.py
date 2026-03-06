# DEFINITION: 
# Short hand if-else is a way to write an if-else block in one line.
# Syntax: [Result_if_True] if [Condition] else [Result_if_False]

a = 330
b = 3303

# MAIN POINT: Read it like a sentence: "Print A if a is greater than b, else print B"
print("A") if a > b else print("B")

# Example with variable assignment
result = "Greater" if a > 500 else "Smaller"
print(result)

# MAIN POINT: You can also use it for multiple conditions (though it gets messy)
print("A") if a > b else print("=") if a == b else print("B")