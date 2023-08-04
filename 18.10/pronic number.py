import math
n=int(input())
a=int(math.sqrt(n))
count=0
for i in range(1,n):
    if(n%i==0 and n%i+1==n//i):
        count+=1
    elif(n%i-1==n//i):
        count+=1
    else:
        continue
if(count==1):
    print("yes")
else:
    print("no")
