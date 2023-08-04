n=list(map(int,input().split()))
k=int(input())
i=0
j=len(n)-1
m=0
c=0
while(i<=j):
    if(n[i]==k and c==0):
        c=i+1
    if(n[j]==k and m==0):
        m=j+1
    if(c!=0 and m!=0):
        break
    i+=1
    j-=1
if(c!=0 and c!=m):
    print(m-c)
elif(c==0 and m==0):
    print("-1")
elif(m==c):
    print("0")
        
        
        
