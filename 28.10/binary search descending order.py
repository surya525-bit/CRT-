l=list(map(int,input().split()))
k=int(input())
c=0
i=0
j=len(l)-1
while(i<=j):
    mid=(i+j)//2
    if(k>l[mid]):
        j=mid-1
    if(k<l[mid]):
        i=mid+1
    if(k==l[mid]):
        c=1
        print(mid+1)
        break
if(c==0):
    print("element not found")
