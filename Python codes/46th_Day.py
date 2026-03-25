# --- THEORY: ANONYMOUS FUNCTIONS ---

# Regular function vs Lambda
def double(x):
    return x * 2

# REMEMBER: 'double_lambda' is the variable holding the function
double_lambda = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double_lambda(5)) # Output: 10
print(avg(3, 5, 10))    # Output: 6.0

# WARNING: Don't use lambdas for complex logic. Use 'def' for readability.