# Open the file in read mode
with open('myfile.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line: # If line is empty, we reached the end of the file
            break
        print(line) # NOTE: This will print an extra newline because the file has \n

# Open the file
with open('myfile.txt', 'r') as f:
    lines = f.readlines() # Returns a LIST: ["Line 1\n", "Line 2\n", "Line 3\n"]
    
    # Accessing specific lines by index
    print(lines[0]) # Prints the first line
    
    # Iterating through the list
    for line in lines:
        print(line.strip()) # .strip() removes the \n at the end

lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

with open('output.txt', 'w') as f:
    # NOTE: writelines does NOT add newlines automatically. 
    # You must include \n in your strings manually!
    f.writelines(lines)