
day_num = int(input("Enter number (1-7): "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 1 <= day_num <= 7:
    print("Day is:", days[day_num - 1])
else:
    print("Invalid number")