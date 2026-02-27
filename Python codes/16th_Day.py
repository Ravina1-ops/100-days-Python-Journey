# While Loop 

# The secret number guessing game

secret_number = 8
g = int(input("Guess the secret number: "))
while(g != secret_number):
    print("Oops, Sorry Your guess is wrong. Try Again")
    g = int(input("Guess the secret number: "))
print("You found the secret")

# Summing the fly numbers 

total = 0
num = int(input("Enter number one by one to add them: "))
while num != 0:
    total += num
    print("The current total is: ", total)
    num = int(input("Enter number one by one to add them: "))
print("Finished, Your total is: ", total)
   