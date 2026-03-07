import random

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]
    
    print("--- Rock, Paper, Scissors: The Ultimate Showdown ---")
    
    while True:
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
        user_choice = input("Enter Rock, Paper, or Scissors (or 'q' to quit): ").lower()
        
        if user_choice == 'q':
            break
            
        if user_choice not in options:
            print("That's not a valid move. Try again!")
            continue

        # This makes the computer's move unpredictable every round
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Logic to determine the winner and update scores
        if user_choice == computer_choice:
            print("Result: It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("Result: You win this round! 🎉")
            user_score += 1
        else:
            print("Result: Computer wins this round! 🤖")
            computer_score += 1

    print("\n--- FINAL SCORE ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("You are the grand champion!")
    elif user_score < computer_score:
        print("The machines have won this time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()