m,n=map(int,input().split())
l2=[]
d=0
for i in range(m,n+1):
    l1=[]
    s=0
    a=i
    while(a!=0):
        r=a%10
        s=s+r
        a=a//10
        l1.append(r)
    k=max(l1)
    if(s-k==k):
        l2.append(i)
for i in l2:
    d=d+i
print(d)

        
