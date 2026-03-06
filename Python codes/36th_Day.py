# DEFINITION: 
# The enumerate() function adds a counter to an iterable and returns it 
# as an enumerate object (pairs of index and value).

marks = [12, 56, 32, 98, 12, 45, 1, 4]

# MAIN POINT: Without enumerate, you'd do: index = 0; for mark in marks: index += 1
# With enumerate, you get 'index' and 'mark' in one go.

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")

# MAIN POINT: You can change the starting index by providing a 'start' argument
# By default it starts at 0, but here we start at 1
for index, mark in enumerate(marks, start=1):
    print(f"Student {index} got {mark} marks")