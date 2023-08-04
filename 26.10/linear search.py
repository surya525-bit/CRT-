n=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(n)):
    if(n[i]==k):
        c=i
        break
if(c!=0):
    print(c+1)
else:
    print("-1")
