x = int(input("Enter your today's Percentage Score: "))
match x:
    case n  if(n<50):
            print("Grade: D 'Not so good need a lot of time management.'")
    case n if(n>50 and n<70):
            print("Grade: C 'Hmm ok ok but needs more disciplie '")
    case n if(n>70 and n<85):
            print("Grade: B 'Good efforts today.Maintain consistency'") 
    case n if(n>85 and n<100):
            print("Grade: A 'Excellent work today. Keep it up.'")
    case _:
        print("Are you sure that's a real day? Check your spelling, Boss!")