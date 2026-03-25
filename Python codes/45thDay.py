# --- THEORY: PRECISION FILE HANDLING ---

with open('test.txt', 'w') as f:
    f.write("Hello World")

with open('test.txt', 'r') as f:
    # 1. Move to the 6th character (after 'Hello ')
    f.seek(6)
    
    # 2. Check where we are
    print(f"Current cursor position: {f.tell()}") # Output: 6
    
    # 3. Read from this position
    data = f.read(5) 
    print(data) # Output: World

# --- THEORY: TRUNCATING ---
with open('sample.txt', 'w') as f:
    f.write("This is a very long sentence.")
    # REMEMBER: truncate(n) makes the file exactly 'n' bytes long.
    f.truncate(5) 

with open('sample.txt', 'r') as f:
    print(f.read()) # Output: 'This ' (The rest is deleted forever!)