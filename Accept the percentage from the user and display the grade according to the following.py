
p = int(input("Enter percentage: "))
if p < 25:
    print("Grade: D")
elif p <= 45:
    print("Grade: C")
elif p <= 65:
    print("Grade: B")
elif p <= 85:
    print("Grade: A")
else:
    print("Grade: A+")