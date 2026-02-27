''' Doc string are string literals that apppear right after
 the definition of a function ,method ,class or module'''

def square(n):
    '''Take a number n and return its square value'''
    print(n**2)
square(7)
print(square.__doc__)

# above is the syntax to print doc string of a function

"""comments or docstring me main difference
hai ki docstring humesha function
ki next line me likhi jayagi otherwise vo ak comment 
consider kiya jayaga """

def square2(n):
    print(n)
    '''Take a number n and return its 
    square value'''
    print(n**2)
square2(7)
print(square2.__doc__)
# iski docstring none hogi kyoki ye just after func nhi likhi hai


# pep 8 = python enhancement proposal
# it provide guidelines and bes practice to write python code
# import this = poem by tim peters Zen of python print hoga
