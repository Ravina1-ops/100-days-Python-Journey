# local vs global variable
# --- THEORY ---
# 1. Global: Accessible throughout the file.
# 2. Local: Temporary; born inside a function, dies when function finishes.
# 3. 'global' keyword: Without this, you CANNOT change a global variable inside a function.

x = 10  # GLOBAL

def my_func():
    # REMEMBER: Use this keyword ONLY when you must modify the external 'x'
    global x 
    x = 5     # Modifying global variable
    y = 7     # LOCAL (Invisible to code outside this function)
    print(f"Inside: local y is {y}")

my_func()
print(f"Outside: global x is now {x}") 

# WARNING: Accessing 'y' here will cause a NameError.