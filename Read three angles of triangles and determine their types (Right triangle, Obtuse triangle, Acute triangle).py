
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    if 90 in (a, b, c):
        print("Right Triangle")
    elif any(angle > 90 for angle in (a, b, c)):
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Not a valid triangle")