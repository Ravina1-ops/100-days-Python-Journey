# --- THEORY: IDENTITY VS EQUALITY ---

# Case 1: Lists (Mutable)
a = [1, 2, 43]
b = [1, 2, 43]

print(a == b) # True: The values inside the lists are identical.
print(a is b) # False: Python creates two different objects in memory.

# Case 2: Constants and Integers (Immutable)
# Python optimizes memory for small integers and strings (Interning)
x = 5
y = 5

print(x == y) # True: Values are same.
print(x is y) # True: Python points both to the same '5' object to save RAM.

# Case 3: Strings
name1 = "Ravina"
name2 = "Ravina"

print(name1 == name2) # True
print(name1 is name2) # True (due to Python String Interning)

# Case 4: None
z = None
# PRO TIP: It is a best practice to use 'is' with None
print(z is None) # True