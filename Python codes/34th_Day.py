#  raising custom error in python
# THEORY: Why raise custom errors?
# 1. To stop the program execution when a specific condition is met.
# 2. To provide meaningful error messages to the user or developer.
# 3. To ensure that the program doesn't proceed with "bad" or "illegal" data.

# EXAMPLE 1: Raising a built-in error with a custom message
a = int(input("Enter any value between 5 and 9: "))

if(a < 5 or a > 9):
    # 'raise' is the keyword used to stop the program and show an error
    # 'ValueError' is a built-in Python error class
    raise ValueError("Value should be between 5 and 9")

# This line will ONLY execute if no error was raised above
print(f"You entered: {a}")


# THEORY: Defining your own Error Classes
# In Python, we can create our own error types by creating a class 
# that "inherits" from the built-in Exception class.
class CustomError(Exception):
    # This class can be empty or have logic to handle the error
    pass

# We can then raise our own specific error
# raise CustomError("This is a custom error message")


# EXAMPLE 2: A practical check (like Harry's 'quit' example)
user_input = input("Enter 'quit' to exit or a number: ")

if user_input != "quit":
    try:
        num = int(user_input)
        print(f"Your number is {num}")
    except ValueError:
        # If the user didn't type 'quit' AND didn't type a number
        raise TypeError("Input must be 'quit' or an integer!")