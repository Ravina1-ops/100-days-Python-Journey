# Recursion in python 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
     return n*factorial(n-1)
print(factorial(5))
print(factorial(4))

def fibonacci(m):
   f0 = 0
   f1 = 1
   if(m == 1):
      print(f0)
   if(m==2):
      print(f1)
   else:
       for p in range(m):
        p = f0 + f1
        print(p)
        f0 = f1
        f1 = p

print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(7))