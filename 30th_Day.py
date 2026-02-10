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