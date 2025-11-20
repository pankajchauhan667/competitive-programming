t=int(input())
for _ in range(t):
    s=input()
    v=0
    c=0
    for ch in s:
        if ch.lower() in "aeiou":
            v+=1
        elif ch.isalpha():
            c+=1
    print(v,c)
