import math
n=int(input())
def prime(p):                    #prime number?:
    c=0
    a=(int(math.sqrt(p))+1)
    for i in range(2,a):
        if(p%i==0):
            c+=1
            break
    if(c==1):
        return 0
    else:
        return 1                #prime number?:
p=prime(n)
l=[]
if(n>10 and p==1):
    print("INVALID")
if((n>10 and p==0)): #prime factors
    i=2
    while(n>1):
        if(n%i==0):
            n=n//i
            l.append(i)
        else:
            i+=1         #storing prime factors
    s=1
    s1=""
    count=0
    for i in range(len(l)):
        if(l[i]>10):
            print("INVALID")
            count=1
            break
        if(s*l[i]<10):
            s=(s*l[i])
        elif(s*l[i]>=10):
            s1=s1+str(s)
            s=1
            s=(s*l[i])
        if(i==len(l)-1):
            s1=s1+str(s)
    if(count==0):
        print(s1)
if(n<10):
    s="1"+str(n)
    print(s)
