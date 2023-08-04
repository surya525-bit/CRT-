l=list(map(int,input().split()))
for i in range(len(l)-2):
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            c=l[j]
            l[j]=l[j+1]
            l[j+1]=c
print(l)
