def count(n):
    if n==0:
        return 0
    return 1+count(n//10)

n=int(input())
print(1 if n==0 else count(n))
