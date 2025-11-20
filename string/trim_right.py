s=input()
i=len(s)-1
while i>=0 and s[i]=='*':
    i-=1
print(s[:i+1])
