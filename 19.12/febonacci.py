n=int(input())
def feb(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    else:
        f=feb(n-1)+feb(n-2)
        return f
f=feb(n)
print(f)
