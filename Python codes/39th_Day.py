# OS module
# --- THEORY ---
# 1. os.mkdir: Create one folder.
# 2. os.makedirs: Create folders inside folders.
# 3. os.listdir: See everything inside a folder.
# 4. os.getcwd: Find out where you are currently (Current Working Directory).

import os

# REMEMBER: Always check if a folder exists before creating it to avoid errors.
if not os.path.exists("Tutorials"):
    os.mkdir("Tutorials")

# Automated folder creation for 100 days
# for i in range(1, 101):
#     os.mkdir(f"Tutorials/Day{i}")

# REMEMBER: os.listdir returns a LIST of strings (filenames).
folders = os.listdir(".")
print(f"Files in this folder: {folders}")