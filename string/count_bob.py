s=input()
c=0
for i in range(len(s)-2):
    if s[i:i+3]=="bob":
        c+=1
print(c)
