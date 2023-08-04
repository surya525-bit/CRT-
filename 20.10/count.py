l1=list(map(int,input().split()))
m=max(l1)
m2=abs(min(l1))
l2=[0]*(m+1)
l3=[0]*(m2+1)
for i in l1:
    if(i>=0):
        l2[i]+=1
for i in l1:
    if(i<0):
        l3[i]+=1
for i in l1:
    if(i>=0):
        print(l2[i],end=" ")
    if(i<0):
        print(l3[i],end=" ")
        
