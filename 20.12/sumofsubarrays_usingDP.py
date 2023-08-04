l=list(map(int,input().split()))
s=int(input("sum="))
m=[]
for i in range(len(l)):
    t=[0]*(s+1)
    m.append(t)
    m[i][0]=1
for i in range(len(l)):
    for j in range(s+1):
        if(j<l[i]):
            m[i][j]=m[i-1][j]
        elif(j==l[i]):
            m[i][j]=1
        elif(j>l[i]):
            m[i][j]=max(m[i-1][j-l[i]],m[i-1][j])
if(m[len(l)-1][s]==1):
    print("True")
else:
    print("False")
