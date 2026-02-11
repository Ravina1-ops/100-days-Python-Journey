# loops with else statement

for i in range(5):
    print(i)
    if i == 4:
        break # If this hits, the 'else' will NOT run
else:
    print("Sorry, no i")

# Example where else DOES run:
for x in []:
    print(x)
else:
    print("Loop finished successfully (even if empty)")