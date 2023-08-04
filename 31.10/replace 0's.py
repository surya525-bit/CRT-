l=list(map(int,input().split()))
k=int(input())
i=0
j=0
r=0
m=0
while(j<len(l)-1):
    if(l[j]==0 and r<k):
        r+=1
    if(m<j-i):
        m=j-i
    elif(l[j]==0 and r>=k):
        if(l[i]==0):
            r-=1
        i+=1
    j+=1
if(m!=0):
    print(m)
else:
    print(len(l))
