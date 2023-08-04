l=input("enter the String ")
l1=input("enter the String ")
m=[]
for i in range(0,len(l)+1):
    t=[0]*(len(l1)+1)
    m.append(t)
for i in range(len(l)+1):
    for j in range(len(l1)+1):
        if(i>0 and j>0):
            if(l[i-1]==l1[j-1]):
                m[i][j]=m[i-1][j-1]+1
            else:
                m[i][j]=max(m[i][j-1],m[i-1][j])
for i in range(len(l)+1):
    print(m[i])
    p=m[len(l)][len(l1)]
print(p)

i=1
j=1
f=0
while(1):
    if(m[i][j]!=m[i][j-1]):
        print(l1[j-1],end="")
        f=1
    if(f==0):
        i=i+1
        if(i==len(l)):
            f=1
    else:
        f=0
        j=j+1
        i=1
    if(m[i][j]==p):
        print(l1[j-1],end="")
        break
        
        


    
                
            
                   
                   
