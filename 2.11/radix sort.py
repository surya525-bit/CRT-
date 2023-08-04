import math
l=list(map(int,input().split()))
f=[0]*10
c=int(math.log(a,10))+1
for i in range(len(l)):
    f[l[i]%10]+=1
for i in range(1,len(f)):
    f[i]+=f[i-1]

    
