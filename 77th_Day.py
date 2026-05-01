Create a function that takes a list of numbers and return the number that's unique.
87/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
Examples
unique([3, 3, 3, 7, 3, 3]) 
➞ 7
unique([0, 0, 0.77, 0, 0]) 
➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) 
Notes
➞ 0
Test cases will always have exactly one unique number while all others are the same.
In [223]:
In [224]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
def unique(numbers):
# Use a dictionary to count occurrences of each number
count_dict = {}
# Count occurrences of each number in the list
for num in numbers:
if num in count_dict:
count_dict[num] += 1
else:
count_dict[num] = 1
# Find the unique number (occurs only once)
for num, count in count_dict.items():
if count == 1:
return num
1
unique([3, 3, 3, 7, 3, 3]