#  kaun banega crorepati 

# List of dictionaries to store Question, Options, and the Correct Answer
questions = [
    {
        "question": "Which language is used for Android Development?",
        "options": ["Python", "Java", "Swift", "PHP"],
        "answer": 2 # Index 2 is Java (1-based for user input)
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["Newton", "Einstein", "Charles Babbage", "Tesla"],
        "answer": 3
    },
    {
        "question": "Which of these is a Set in Python?",
        "options": ["[]", "{}", "()", "set()"],
        "answer": 4
    }
]

# Prize money for each level
levels = [1000, 5000, 10000, 50000, 100000]
money = 0

print("--- Welcome to Kaun Banega Crorepati ---")

for i in range(len(questions)):
    q_data = questions[i]
    
    print(f"\n\nQuestion for Rs. {levels[i]}:")
    print(f"Q: {q_data['question']}")
    print(f"1. {q_data['options'][0]}       2. {q_data['options'][1]}")
    print(f"3. {q_data['options'][2]}       4. {q_data['options'][3]}")
    
    # Exception Handling to prevent crash if user enters a string
    try:
        reply = int(input("Enter your answer (1-4) or 0 to quit: "))
        
        if reply == 0:
            print("You chose to quit.")
            break
            
        if reply == q_data["answer"]:
            print(f"CORRECT! You have won Rs. {levels[i]}")
            money = levels[i]
        else:
            print("WRONG ANSWER! Game Over.")
            # Based on Harry's logic, if you get it wrong, you take home the last safe money
            break
            
    except ValueError:
        print("Invalid input! Please enter a number (1-4).")
        break

print(f"\nYour final take-home prize money is: Rs. {money}")
print("Thank you for playing!")