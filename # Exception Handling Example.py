# Exception Handling Example

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print(f"Division successful. Result: {result}")
        return result
    finally:
        print("Division attempt finished.")

print("--- Test Case 1: Successful Division ---")
output1 = divide(10, 2)
print(f"Returned value: {output1}\n")

print("--- Test Case 2: Division by Zero ---")
output2 = divide(10, 0)
print(f"Returned value: {output2}\n")

print("--- Test Case 3: Invalid Input Type ---")
output3 = divide(10, "a")
print(f"Returned value: {output3}\n")