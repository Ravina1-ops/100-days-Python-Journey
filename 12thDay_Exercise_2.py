# Greetings program 

t = int(input("What time is it (hour only): "))
s = input("a.m/p.m : ").lower() # .lower() handles "PM", "pm", or "p.m"

if t <= 0 or t > 12:
    print("Invalid hour! Please use 1-12.")

elif s == "a.m":
    print("Good Morning Sir/Mam.")

elif s == "p.m":
    if t == 12 or t < 4:
        print("Good Afternoon Sir/Mam.")
    elif 4 <= t < 9:
        print("Good Evening Sir/Mam.")
    else:
        # This catches 9, 10, and 11 p.m.
        print("Good Night Sir/Mam. Sweet dreams!")

else:
    print("Invalid input for a.m/p.m.")
