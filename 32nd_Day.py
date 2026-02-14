# Exception Handling
a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    # This runs only if there is an error in the 'try' block
    print(f"Invalid Input! Error: {e}")

print("End of program") # This will still print even if an error occurred

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num]) # This could cause an IndexError if num > 1
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error: That position doesn't exist in the list.")