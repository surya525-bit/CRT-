l=list(map(int,input().split()))
k=0
for i in l:
    a=0
    for j in l:
        if(i==j):
            a=a+1
    print(a,end=" ")
print()
for i in range(len(l)):
    a=0
    for j in range(i+1):
        if(l[i]==l[j]):
            a=a+1
    print(a,end=" ")
print()
for i in range(len(l)):
    a=0
    for j in range(i,len(l)):
        if(l[i]==l[j]):
            a=a+1
    print(a,end=" ")
print()        

        
        
        


