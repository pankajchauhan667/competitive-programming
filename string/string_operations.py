s=input()
s=s+s
s=''.join(ch for ch in s if not ch.isupper())
res=''
for ch in s:
    if ch in 'aeiou':
        res+='#'
    else:
        res+=ch
print(res)
