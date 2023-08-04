n=int(input("enter the length "))
l=list(map(int,input("enter the price array ").split()))
m=[]
for i in range(0,len(l)):
    t=[0]*(n+1)
    m.append(t)
for i in range(0,len(l)):
    for j in range(0,n+1):
        if(i==0):
            m[i][j]=l[i]*j
        elif(i!=0 and j<=i):
            m[i][j]=m[i-1][j]
        elif(i!=0 and j>i):
            m[i][j]=max(m[i][j-i-1]+l[i],m[i-1][j])

for i in range(len(l)):
    print(m[i])
p=m[len(l)-1][n]
print(p)

while(j!=0):
    if(i==0):
        print(i+1,end=" ")
        a=j-(i+1)
        i=n-1
    elif(m[i][j]==m[i-1][j]):
        i=i-1
    else:
        print(i+1,end=" ")
        a=j-(i+1)
        j=a

#enter the length 11
#enter the price array 3 9 13 12 8 12 8 8 3 10 13
            
            
