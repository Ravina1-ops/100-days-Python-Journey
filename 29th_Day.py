# set in python 
# Creating a set
s = {2, 4, 2, 6}
print(s) 
# Output: {2, 4, 6} (Notice duplicate 2 is gone and order is not guaranteed)

# Creating an empty set
harry = set() # You MUST use set(), because {} creates an empty dictionary
print(type(harry))

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# Union: Combines all elements from both sets
print(s1.union(s2)) # {1, 2, 3, 5, 6, 7}

# Intersection: Only elements present in BOTH sets
print(s1.intersection(s2)) # {6}

# Update: Adds elements of s2 into s1 permanently
s1.update(s2)
print(s1) # s1 is now {1, 2, 3, 5, 6, 7}

cities1 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities2 = {"Seoul", "Kabul", "Delhi"}

# Symmetric Difference: Elements NOT common to both ( (A∪B) - (A∩B) )
cities3 = cities1.symmetric_difference(cities2)
print(cities3) # {'Tokyo', 'Madrid', 'Delhi'}

# Difference: Elements present only in the first set
cities4 = cities1.difference(cities2)
print(cities4) # {'Tokyo', 'Madrid'}

cities = {"Tokyo", "Madrid", "Delhi", "Berlin"}

# isdisjoint(): Returns True if no items are common
c1 = {"Tokyo", "Madrid"}
c2 = {"Delhi", "Berlin"}
print(c1.isdisjoint(c2)) # True

# issuperset() and issubset()
print(cities.issuperset(c1)) # True (cities contains all of c1)
print(c1.issubset(cities))   # True (c1 is inside cities)

# Adding items
cities.add("Helsinki")

# Removing items
cities.remove("Tokyo") # Raises error if item not found
cities.discard("London") # Does NOT raise error if item not found (Safer)

# pop(): Removes a random item
item = cities.pop()
print(item)

# clear(): Deletes all items
cities.clear()

