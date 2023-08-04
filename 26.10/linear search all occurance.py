n=list(map(int,input().split()))
k=int(input())
c=0
m=0
for i in range(len(n)):
    if(n[i]==k):
        c=i+1
        print(c,end=" ")
if(c==0):
    print("-1")
