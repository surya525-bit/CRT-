l=list(map(int,input().split()))
b=int(len(l)/2)-1
le=len(l)
r=int(input())
r=r%len(l)
for i in range(r):
    c=l[b]
    for j in range(b,0,-1):
        a=l[j]
        l[j]=l[j-1]
    l[0]=c 
for i in range(r):
    c=l[b+1]
    for j in range(b+1,le-1):
        l[j]=l[j+1]
    l[le-1]=c
print(l)
