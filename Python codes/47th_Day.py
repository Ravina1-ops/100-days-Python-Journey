from functools import reduce

# --- 1. MAP ---
# Goal: Square every number in the list
numbers = [1, 2, 3, 4, 5]
# REMEMBER: map returns a 'map object', so convert it back to a list!
squared = list(map(lambda x: x * x, numbers))
print(f"Squared: {squared}") # [1, 4, 9, 16, 25]

# --- 2. FILTER ---
# Goal: Keep only numbers greater than 2
# REMEMBER: The function must return True or False.
greater_than_2 = list(filter(lambda x: x > 2, numbers))
print(f"Filtered: {greater_than_2}") # [3, 4, 5]

# --- 3. REDUCE ---
# Goal: Sum all numbers (1+2+3+4+5)
# REMEMBER: It takes two arguments (current_sum, next_value).
total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Total Sum: {total_sum}") # 15