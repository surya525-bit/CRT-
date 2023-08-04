l=list(map(int,input().split()))
b=len(l)
lr=int(input("left:"))
rr=int(input("right:"))
for i in range(lr):
    c=l[b-1]
    for j in range(b-1,0,-1):
        a=l[j]
        l[j]=l[j-1]
    l[0]=c
print(l)
for i in range(rr):
    c=l[0]
    for j in range(b-1):
        l[j]=l[j+1]
    l[b-1]=c
print(l)

        
