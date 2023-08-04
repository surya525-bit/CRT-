l=list(map(int,input().split()))
p=int(input('p: '))
q=int(input('q: '))
le=len(l)
r=int(input("no.of rotations: "))
r=r%len(l)
for i in range(r):
    c=l[q]
    for j in range(q,p,-1):
        a=l[j]
        l[j]=l[j-1]
    l[p]=c 
print(l)
