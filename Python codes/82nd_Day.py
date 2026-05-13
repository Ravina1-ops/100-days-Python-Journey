Write a Python program to print all pronic numbers between 1 and 100.
A pronic number, also known as an oblong number or rectangular number, is a type of
figurate number that represents a rectangle. It is the product of two consecutive integers, n
and (n + 1). Mathematically, a pronic number can be expressed as:
𝑃𝑛
= 𝑛∗(𝑛+1)
For example, the first few pronic numbers are:
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
𝑃1
𝑃2
𝑃3
𝑃4
= 1∗(1+1) = 2
= 2∗(2+1) = 6
= 3∗(3+1) = 12
= 4∗(4+1) = 20
def is_pronic_number(num):
for n in range(1, int(num**0.5) + 1):
if n * (n + 1) == num:
return True
return False
print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
if is_pronic_number(i):
print(i, end=" | ")