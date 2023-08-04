import math
l=list(map(int,input().split()))
a=max(l)
p=0
i=2
l1=[]
while(p<a):
    k=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            k+=1
    if(k==0):
        p=p+1
        l1.append(i)
    i=i+1
for i in l:
    print(l1[i-1],end=" ")
