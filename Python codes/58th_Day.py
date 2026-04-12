class Math:
    def __init__(self, num):
        self.num = num

    # Instance Method: Needs 'self' to access the object's number
    def add_to_num(self, n):
        self.num = self.num + n

    # STATIC METHOD: Does NOT need 'self'
    # Use the @staticmethod decorator
    @staticmethod
    def add(a, b):
        return a + b

# --- HOW TO USE ---

# 1. You can call it through the CLASS (No object needed!)
result1 = Math.add(5, 5)
print(result1) # Output: 10

# 2. You can also call it through an INSTANCE
a = Math(5)
print(a.add(7, 2)) # Output: 9