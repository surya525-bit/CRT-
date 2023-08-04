n=list(map(int,input().split()))
l=[0]*(len(n))
for i in range(len(n)):
    l[i]=n[-(i+1)]
print(l)
