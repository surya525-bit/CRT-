l=list(map(int,input().split()))
i=0
count=0
j=len(l)-1
while(i<j):
    if(l[i]==l[j]):
        count+=1
    i+=1
    j-=1
if(count==len(l)//2):
    print("palindrome")
else:
    print("no")
        
