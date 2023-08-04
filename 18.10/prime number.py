import math
n=int(input())
a=int(math.sqrt(n))
c=0
if(n!=0):
    for i in range(2,a+1):
        if(n%i==0):
            c=c+1
if(c>=1):
    print("not prime")
if(c==0):
    print("prime")
if(n==1):
    print("neither prime nor composite")
if(n<=0):
    print("enter a positive integer")
