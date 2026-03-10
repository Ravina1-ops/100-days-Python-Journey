# File IO 
# --- THEORY ---
# 'r' = Read (Default)
# 'w' = Write (Deletes everything in file first and writes fresh)
# 'a' = Append (Adds to the end of existing text)

# REMEMBER: Always close a file using f.close(). If you don't, 
# you might face "file in use" errors or memory leaks.

f = open('myfile.txt', 'w')
f.write("Harry says: Practice makes perfect!")
f.close() 

f = open('myfile.txt', 'r')
content = f.read()
print(content)
f.close()