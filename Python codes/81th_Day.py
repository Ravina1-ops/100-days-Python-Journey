# Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

class DivisibleBySeven:
def __init__(self,n):
self.n = n
def generate_divisible_by_seven(self):
for num in range(self.n + 1):
if num%7 == 0:
yield num
49/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [43]:
1
2
3
4
5
6
n = int(input("Enter your desired range: "))
divisible_by_seven_generator = DivisibleBySeven(n).generate_divisible_b
for num in divisible_by_seven_generator:
print(num)