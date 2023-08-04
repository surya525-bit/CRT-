l=list(map(int,input().split()))
i=0
c=0
j=len(l)-1
while(i<=j):
    if(l[i]==l[j]):
        c=0
    else:
        c=1
        break
    i+=1
    j-=1
if(c==0):
    print("palindrome")
else:
    print("no")
        
