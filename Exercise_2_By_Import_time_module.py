import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(timestamp)
hour = int(input("Enter Hour: "))
print(hour)
if(hour>0 and hour<12):
    print("Good morning.")
elif (hour== 12 and hour <16) :
    print("Good afternoon.")
else :
    print("Good Evening.")
    