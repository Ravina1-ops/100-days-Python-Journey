class Employee:
    def __init__(self):
        # 1. PUBLIC Access Modifier
        # Can be accessed directly from anywhere
        self.name = "Harry"

        # 2. PRIVATE Access Modifier (Double Underscore)
        # Python "mangles" this name to _Employee__name
        self.__salary = "50000"

    # 3. PROTECTED Access Modifier (Single Underscore)
    # Convention: Only use inside this class or its subclasses
    def _show_privately(self):
        return "This is a protected method"

obj = Employee()

# --- Accessing Public ---
print(obj.name) # Output: Harry

# --- Accessing Private (The WRONG way) ---
# print(obj.__salary) # This will THROW AN ATTRIBUTE ERROR

# --- Accessing Private (The Name Mangling way) ---
# Syntax: _ClassName__VariableName
print(obj._Employee__salary) # Output: 50000

# --- Accessing Protected ---
print(obj._show_privately()) # Output: This is a protected method