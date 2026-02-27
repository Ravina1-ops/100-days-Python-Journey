import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)

num = int(input("Display multiplication table of: "))
for i in range(1, 11):
 print(f"{num} X {i} = {num*i}")