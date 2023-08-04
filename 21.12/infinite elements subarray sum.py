l=list(map(int,input().split()))
s=int(input("enter the sum"))
m=[]
for i in range(0,len(l)):
    t=[99]*(s+1)
    m.append(t)
for i in range(0,len(l)):
    for j in range(0,s+1):
        if(l[i]==j):
            m[i][j]=1
        elif(l[i]<j):
            a=j-l[i]
            if(i==0):
                if(m[i][a]!=99):
                    m[i][j]=m[i][a]+1
            else:
                if(m[i][a]==99):
                    m[i][j]=m[i-1][j]
                else:
                    m[i][j]=min(m[i][a]+1,m[i-1][j])
for i in range(0,len(l)):
    for j in range(0,s+1):
        print(m[i][j],end="\t")
    print()
print(m[len(l)-1][s])

#9 6 5 1
#11
                    
            
'''
l=list(map(int,input().split()))
s=int(input("enter the sum"))
b=s
m=[]
for i in range(0,len(l)):
    t=[0]*(s+1)
    m.append(t)
for i in range(0,len(l)):
    for j in range(0,s+1): 
        if(i==0 and j%l[i]==0):
            m[i][j]=j//l[i]
        else:
            if(j<l[i]):
                m[i][j]=m[i-1][j]
            else:
                if(j%l[i]==0 and m[i-1][j]>0):
                    m[i][j]=min(j//l[i],m[i-1][j])
                elif(j%l[i]==0 and m[i-1][j]==0):
                    m[i][j]=j//l[i]
                else:
                    p=s
                    q=j
                    c=0
                    while(1):
                        if(q%l[i]!=0):
                            q=q-l[i]
                            if(m[i][q]!=0):
                                c=1+m[i][q]
                                q=0
                        if(q<=0):
                            break
                    if(c==0):
                        m[i][j]=m[i-1][j]
                    elif(m[i-1][j]==0):
                        m[i][j]=c
                    else:    
                        m[i][j]=min(c,m[i-1][j])
print(m[len(l)-1][s])

        

'''
