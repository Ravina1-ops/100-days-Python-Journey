# getter setter in oops
class MyClass:
    def __init__(self, value):
        # We use _value (internal naming) to store the actual data
        # This prevents a 'RecursionError' when the getter/setter has the same name
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # --- THE GETTER ---
    # The @property decorator turns this method into a 'getter'
    # It allows us to access 'ten_value' like a variable (obj.ten_value)
    # instead of a function (obj.ten_value())
    @property
    def ten_value(self):
        return 10 * self._value

    # --- THE SETTER ---
    # The @name.setter decorator allows us to 'set' a value to the getter name
    # Syntax: @<getter_name>.setter
    @ten_value.setter
    def ten_value(self, new_value):
        # This is where you can add VALIDATION logic
        # For example, checking if the value is a number or within a range
        print("Setter is being called to update the value...")
        self._value = new_value / 10

# 1. Creating the object
obj = MyClass(10)

# 2. Using the GETTER
# Note: No parentheses used here! It looks like a property/attribute.
print(f"Initial 10x value: {obj.ten_value}") 

# 3. Using the SETTER
# This triggers the @ten_value.setter method automatically
obj.ten_value = 67 

# 4. Checking the results
print(f"New 10x value: {obj.ten_value}")
obj.show() # Original value is now 6.7