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

def recur_fibo(n):
 if n <= 1:
  return n
 else:
  return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = int(input("Enter the number of terms (greater than 0): "))
# check if the number of terms is valid
if nterms <= 0:
 print("Plese enter a positive integer")
else:
 print("Fibonacci sequence:")
for i in range(nterms):
 print(recur_fibo(i))