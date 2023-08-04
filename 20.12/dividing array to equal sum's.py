l=list(map(int,input().split()))
if(sum(l)%2!=0):
    print("False")
else:
    s=sum(l)//2
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
                m[i][j]=(m[i-1][j-l[i]])
    c=0
    for i in range(s+1):
        if(m[len(l)-1][i]==1):
            c=1
            break
    if(c==1):
        print("True")
    else:
        print("False")
