#  Time Module
import time

def usingWhile():
    i = 0
    while i < 5000:
        i += 1
        print(i)

init = time.time()
usingWhile()
print(time.time() - init) # Checks execution time

time.sleep(2) # Pauses program for 2 seconds
print("This printed after 2 seconds")