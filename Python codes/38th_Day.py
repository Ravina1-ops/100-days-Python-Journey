# If __name__ = "__main__"
# --- THEORY ---
# This check detects if the file is being run directly or imported.
# REMEMBER: '__name__' is a special variable. 
# If running file directly -> __name__ is "__main__"
# If file is imported -> __name__ is "filename"

def welcome():
    print("Welcome to Harry's module!")

# REMEMBER: Use this to prevent your test code/prints from running 
# when you import this file into another project.
if __name__ == "__main__":
    print("This runs only when you click 'Run' on this file.")
    welcome()