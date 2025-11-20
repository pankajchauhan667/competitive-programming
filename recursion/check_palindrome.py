def pal(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return pal(s,l+1,r-1)

s=input()
print("Palindrome" if pal(s,0,len(s)-1) else "Not Palindrome")
