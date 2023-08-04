n=list(map(int,input().split()))
k=int(input())
c=0
m=0
for i in range(len(n)):
    if(n[i]==k):
        c=i+1
        if(m==0):
            m=i+1
if(c!=0 and c!=m):
    print(c-m)
elif(c==0 and m==0):
    print("-1","-1",sep="\n")
elif(m==c):
    print("0")
