l=list(map(int,input().split()))
a=[0]*(max(l)-min(l)+1)
l1=[0]*len(l)
b=min(l)
for i in l:
    a[i-b]+=1
for i in range(1,len(a)):
               a[i]+=a[i-1]
for i in l:
    l1[a[i-b]-1]=i
    a[i-b]-=1
print(l1)
