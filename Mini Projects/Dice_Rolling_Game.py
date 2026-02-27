''' loop 
Ask: roll the dice?
if user say y
    generate two random numbers
        print them
if user say n
    print thank you message
        terminate
else
    print invalid choice'''

'''.lower() also used to remove a == 'Y' in if condition
using .lower() with input tell the iterpretuer that consider user input 
in lower words. ''' 

import random
count = 0
print("---Welcome to the Dice Roller Game---")
while True:
 a = input("Roll the dice? (y/n): ").lower()

 if a == 'y' :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        count += 1
        print(f'(You rolled a {die1} and a {die2})')
 
 elif a == 'n':
        print("Thanks for playing!")
        print(f'(You rolled the dice {count} times.)')
       
        break
 else:
      print("Invalid Choice!")



