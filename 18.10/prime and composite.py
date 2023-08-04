import math
c=0
p=0
l=list(map(int,input().split()))
for i in l:
    a=int(math.sqrt(i))
    if(i<=1):
        p=p
    else:
        b=0
        for j in range(2,a+1):   
            if(i%j==0):
                b=1              #p=+1
                break
                                 #else:
                                 #    c+=1
        if(b==1):
            p=p+1
        else:
            c=c+1
print(p)
print(c)
            
