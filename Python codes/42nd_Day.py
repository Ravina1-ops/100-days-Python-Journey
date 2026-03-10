# With Statement
# --- THEORY ---
# The 'with' statement is a "Context Manager".
# REMEMBER: You don't need f.close() here. Even if your code crashes 
# mid-way, Python will safely close the file for you.

with open('myfile.txt', 'a') as f:
    f.write("\nThis line was added safely using 'with'.")

# WARNING: Trying to write to 'f' outside the indent will throw an error.