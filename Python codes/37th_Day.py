# how import works 
# --- THEORY ---
# 1. 'import module': Brings everything (math.sqrt).
# 2. 'from module import function': Brings only what you need (sqrt).
# 3. 'import module as m': Gives it a nickname (m.sqrt).

# REMEMBER: Avoid 'from math import *'. It creates confusion 
# because you won't know which function came from where.

import math as m
from math import pi

print(pi) # Directly use the name
print(m.sqrt(16)) # Use the nickname

# REMEMBER: dir() function shows you every tool available in that module.
print(dir(m))