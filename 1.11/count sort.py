l=list(map(int,input().split()))
a=[0]*(max(l)-min(l)+1)
b=min(l)
for i in l:
    a[i-b]+=1
c=0
print(a)
for i in range(len(a)):
    if(a[i]!=0):
        for j in range(a[i]):
            l[c]=i+b
            c+=1
print(l)
