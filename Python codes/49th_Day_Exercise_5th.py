'''
EXERCISE 5: SNAKE WATER GUN
--------------------------

Snake, Water, Gun is a variation of the children's game "Rock Paper Scissors" 
where players use hand gestures to represent a snake, water, or a gun. 
The gun beats the snake, the water beats the gun, and the snake beats the water.

Write a python program capable of playing this game with the user.

RULES:
1. Snake vs. Water: Snake drinks the water --> Snake Wins.
2. Water vs. Gun: Water splashes the gun and makes it useless --> Water Wins.
3. Gun vs. Snake: Gun shoots the snake --> Gun Wins.

GOAL:
- The computer should choose a random option (Snake, Water, or Gun).
- The user should input their choice.
- The program should use conditional logic (if-elif-else) to determine the winner.
- Use a 2D matrix or a simple function to compare choices.
- (Optional) Keep track of the score and play multiple rounds using a loop.

TECHNICAL TOPICS TO USE:
- Random module (random.randint or random.choice)
- Comparison operators
- If-Else logic
- Input handling
'''

# Your code starts here...
import random

def check(comp, user):
  # Returns 1 if User wins, -1 if Computer wins, 0 if Draw
  if comp == user:
    return 0
    
  if(comp == 0 and user == 1): # comp: Snake, user: Water
    return -1
    
  if(comp == 1 and user == 2): # comp: Water, user: Gun
    return -1
    
  if(comp == 2 and user == 0): # comp: Gun, user: Snake
    return -1

  # If none of the above are true, user must have won
  return 1

# 0 for Snake, 1 for Water, 2 for Gun
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water, 2 for Gun: \n"))

score = check(comp, user)

print("You chose: ", user)
print("Computer chose: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == 1):
  print("You Won")
else:
  print("You Lose")