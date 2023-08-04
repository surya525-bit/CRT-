import math
p=int(input())
def prime(n):
    a=int(math.sqrt(n))
    c=0
    if(n!=0):
        for i in range(2,a+1):
            if(n%i==0):
                c+=1
    if(c>=1):
        return False
    else:
        return True
if(prime(p)):
    print(p)
    exit
else:
    i=2
    while(p>1):
        if(p%i==0):
            p=p//i
            print(i)
        else:
            i+=1
        
