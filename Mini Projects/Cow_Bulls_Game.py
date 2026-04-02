''' Cows and Bulls Game 
In this project, you’ll build a game 
where the computer comes up with a secret 4-digit number, and your job is to 
guess it. After each guess, you’ll get feedback in the form of "cows" and "bulls"—
a "bull" means you’ve guessed the right digit in the right spot, while a "cow" 
means the digit is correct but in the wrong spot.'''
import random

def generate_secret():
  digits = list(range(10))
  random.shuffle(digits)
  return ''.join([str(digit) for digit in digits[:4]])


def calculate_cows_and_bulls(secret, guess):
  bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
  cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls

  return cows, bulls


def main():
  secret = generate_secret()
  print('I have generated a 4-digit number with unique digits. Try to guess it!')
  count = 0
  while True:
    guess = input('Guess: ')
    count += 1
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
      cows, bulls = calculate_cows_and_bulls(secret, guess)
      print(f'{cows} cows, {bulls} bulls')

      if bulls == 4:
        print(f'Congratulations! You guessed the correct number in {count} guesses')
        break
    else:
      print('Invalid guess. Please enter a 4-digit number with unique digits.')
      

if __name__ == '__main__':
  main()