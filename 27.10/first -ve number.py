'''l=list(map(int,input().split()))
k=int(input())
i=0
j=k-1
while(j<len(l)):
    a=0
    c=0
    for m in range(i,j+1):
        if(a==0 and l[m]<0):
            a=l[m]
            c=1
            print(a,end=" ")
    if(c==0):
        print("0",end=" ")
    i+=1
    j+=1'''
l=list(map(int,input().split()))
k=int(input())
l1=[]
i=0
j=0
while(j<len(l)):
    if(j-i+1<k):
        j+=1
    if(l[j]<0):
        l1.append(l[j])
    if(j-i+1==k):
        if(len(l1)==0):
            print("0",end=" ")
        elif(l1[0]==l[i]):
            print(l1.pop(0),end=" ")
        else:
            print(l1[0],end=" ")
        j+=1
        i+=1
        
