# Dictonary in python 
# Creating a dictionary
info = {'name': 'Ravina', 'age': 19, 'eligible': True}

# Accessing values
print(info['name'])      # Output: Harry
print(info.get('name'))  # Output: Harry

# The Difference:
# print(info['name2'])   # This throws an ERROR if key doesn't exist
print(info.get('name2')) # This returns 'None' (Safer way)

info = {'name': 'Kajal', 'age': 19, 'eligible': True}

# Accessing all keys
print(info.keys())   # dict_keys(['name', 'age', 'eligible'])

# Accessing all values
print(info.values()) # dict_values(['Karan', 19, True])

# Accessing all Key-Value pairs (Items)
print(info.items())  # Returns a list of tuples

info = {'name': 'Kajal', 'age': 19, 'eligible': True}

# Looping through keys and values using items()
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

ep1 = {122: 45, 123: 89, 567: 69}
ep2 = {222: 67, 566: 90}

# update(): Joins two dictionaries or updates existing keys
ep1.update(ep2)
print(ep1)

# clear(): Removes all items
# ep1.clear()

# pop(): Removes the specified key
ep1.pop(122)

# popitem(): Removes the LAST key-value pair
ep1.popitem()

# del: Removes an item or the whole dictionary
del ep1[123]
# del ep1 # This would delete the entire object