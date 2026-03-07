import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        # Get user input
        user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to stop): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! Final scores soon?")
            break
            
        if user_choice not in options:
            print("Invalid choice. Try again!")
            continue

        # Computer makes a choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🎉")
        else:
            print("You lose! 🤖")
        
        print("-" * 30)

if __name__ == "__main__":
    play_game()