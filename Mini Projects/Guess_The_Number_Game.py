# write a secret number and ask to guess
# if the no is smaller than secret then tell it is smaller and vice versa with higher
# and when the user finds secret number count its guess 

secret_number = 76
# count = 1
print("\n---WELCOME TO GUESSING THE SECRET NUMBER GAME.---")
while True:
    a = input("Want to play the Game? (y/n): ").lower()
    count = 1
    if a == 'y' :
       g = int(input("Guess The number: "))
       while(g!= secret_number):
            count += 1
            if(g > secret_number):
             print("oh! your number is greater than secret number.")
             g = int(input("Guess The number: "))
            else:
                print("Oh! your number is smaller than secret number.")
                g = int(input("Guess The number: "))
       print(f'(Wow You find the secret number in {count} gusses.)')
    elif a == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")