l=list(map(int,input().split()))
k=int(input())
l1=[]
i=0
j=0
while(j<len(l)):
    if(len(l1)==0):
        l1.append(l[j])
    else:
        while(len(l1)>0 and l1[-1]>l[j] ):
            l1.pop(-1)
        l1.append(l[j])
        if(j-i+1==k):
            print(l1[0],end=" ")
            if(l[i]==l1[0]):
                l1.pop(0)
            i+=1
    j+=1
'''5 3 6 14 11 2 3 4 6 1 2 0'''

'''l=list(map(int,input().split()))
k=int(input())
l1=[]
i=0
j=0
l1.append(l[j])
while(j<len(l)-1):
    j+=1
    while(len(l1)>0 and l1[-1]>=l[j] ):
        l1.pop(-1)
    l1.append(l[j])
    if(j-i+1==k):
        if(l[i]!=l1[0]):
            print(l1[0],end=" ")
        if(l[i]==l1[0]):
            print(l1.pop(0),end=" ")
        i+=1
3 3 1 2 2 1 2 1 3 3 1 2 '''
