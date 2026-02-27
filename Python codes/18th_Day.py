a = 9
b = 8
gmean1 = (a * b) / (a + b)
print(gmean1)

c = 8
d = 7
gmean2 = (c * d) / (c + d)
print(gmean2)

def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

calculateGmean(9, 8)
calculateGmean(8, 7)

def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

isGreater(9, 8)
def isLesser(a, b):
    pass  # Placeholder

def average(a=9, b=1):
    print("The average is", (a + b) / 2)

average()          # Uses 9 and 1
average(b=9)       # Uses 9 (default) and 9
average(a=1, b=5)  # Overrides both

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average(5, 6, 7, 1)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)