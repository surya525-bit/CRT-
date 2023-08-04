l=list(map(int,input().split()))
i=0
j=0
while(i<len(l) and j<len(l)):
    if(l[i]%2==0 and l[j]%2!=0):
        t=l[i]
        l[i]=l[j]
        l[j]=t
        i+=1
        j+=1

    if(l[i]%2!=0):
        i+=1

    if(l[j]%2==0):
        j+=1

print(l)
