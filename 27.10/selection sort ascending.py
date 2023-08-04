l=list(map(int,input().split()))
for i in range(len(l)):
    m=i
    t=0
    for j in range(i+1,len(l)):
        if(l[j-1]<=l[j]):
            t+=1
        if(l[j]<l[m]):
            m=j
    c=l[i]
    l[i]=l[m]
    l[m]=c
    if(t==len(l)-i-1):
        break
print(l)
