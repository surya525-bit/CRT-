l=list(map(int,input().split()))
k=int(input())
i=0
j=0
r=0
m=0
while(j<len(l)):
    if(l[j]==0):
        r+=1
    if(r<=k):
        j+=1
    elif(r>k):
        m=max(m,j-i)
        if(l[j]==0):
            r=r-1
            j=j+1
        i+=1
if(m==0):
    print(len(l))
else:
    print(m)
