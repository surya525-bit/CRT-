l=list(map(int,input().split()))
b=len(l)
rr=int(input("right:"))
rr=rr%len(l) #because for the 5th rotation, it is ame as original list
            #similarly 6->1
            #          7->2
for i in range(rr):
    c=l[0]
    for j in range(b-1):
        l[j]=l[j+1]
    l[b-1]=c
print(l)
