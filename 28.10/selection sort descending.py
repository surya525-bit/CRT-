l=list(map(int,input().split()))
for i in range(len(l)):
    m=i
    t=0
    for j in range(i+1,len(l)):
        if(l[j-1]>=l[j] and i==0):
            t+=1
        else:
            t=0
        if(l[j]>l[m]):
            m=j
    if(t==len(l)-1):
        print("not a naive")
        break
    c=l[i]
    l[i]=l[m]
    l[m]=c
print(l)
