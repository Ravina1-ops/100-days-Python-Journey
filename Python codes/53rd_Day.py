# arguments in decorators = *args (taking argument as tuple form)
# ** kwargs (taking arguments as dict form)

import logging

logging.basicConfig(level=logging.INFO, format= '%(message)s')
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b

my_function(2,3)

""" WHY THIS LOGGING EXAMPLE?
1. REAL-WORLD USE CASE: Decorators are most commonly used for 'cross-cutting concerns' 
   like logging, security, or timing. Instead of writing print statements inside every 
   single function, you create one decorator to handle it globally.
2. MONITORING: Logging allows you to track the 'flow' of your program (input -> execution -> output) 
   without interrupting the actual logic of the function.
3. FLEXIBILITY: By using *args and **kwargs, this decorator becomes a 'universal wrapper' 
   that can be applied to any function, regardless of how many arguments it has.

KEY COMPONENTS:
- logging.basicConfig: Essential to set the threshold. By default, Python hides INFO 
  messages. We set it to INFO here so our logs actually appear in the console.
- *args / **kwargs: 'args' handles positional inputs (like 2, 3) as a tuple, while 
  'kwargs' handles named inputs (like a=2, b=3) as a dictionary.
- @log_function_call: This 'syntactic sugar' automatically passes 'my_function' 
  into the decorator.
"""