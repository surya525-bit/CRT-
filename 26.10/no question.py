l=list(map(int,input().split()))
i=0
j=len(l)-1
ls=l[i]
rs=l[j]
while(i!=j):
    if(ls<rs):
        i+=1
        ls+=l[i]
        print("ls:",ls)
    if(ls>rs):
        j-=1
        rs+=l[j]
        print("rs:",rs)
    if(rs==ls and i+1!=j-1):
        i+=1
        ls+=l[i]
        j-=1
        rs+=l[j]
    if(rs==ls and (i+1)==(j-1) ):
        print(i+2)
        break
    

        
        
