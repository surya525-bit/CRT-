def HCF(a,b):
    r=a%b
    while(r>0):
        a=b
        b=r
        r=a%b
    return b
l=list(map(int,input().split()))
if(l[0]>l[1]):
    c=HCF(l[0],l[1])
    lc=(l[0]*l[1])//c
else:
    c=HCF(l[1],l[0])
    lc=(l[0]*l[1])//c
for i in range(2,len(l)):
    if(c>l[i]):
        c=HCF(c,l[i])
        lc=(lc*l[i])//c
    else:
        c=HCF(l[i],c)
        lc=(lc*l[i])//c
print(lc)
