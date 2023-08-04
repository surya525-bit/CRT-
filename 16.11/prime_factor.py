import math
def prime_facts(a):
    l=[]
    for i in range(2,a//2):
        c=0
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                c=1
                break
        if(c==0):
            l.append(i)
    p=0
    while(p<len(l)):
        
        if(a%i==0):
            print(i,end=" ")
            a=a//i
prime_facts(28)
