n=int(input("enter size of queue "))
l=[0]*n
f=-1
r=-1
def Enqueue(data,f,r):
    if(r==n-1):
        if((r+1)%n<f):
            l[(r+1)%n]=data
            r=(r+1)%n
        else:
            print("OverFlow")
    else:
        if((r+1)!=f):
            r=r+1
            l[r]=data
    return r
def Dequeue(f,r):
    if(f==-1):
        print("UnderFlow")
    else:
        l[f]=0
        f=f+1
        if(f==n):
            f=0
    if((f-1)==r):
        f=-1
    return f
def display(f,r):
    if(r>=f):
        for i in range(f,r+1):
            print(l[i])
    if(r<f):
        for i in range(f,n):
            print(l[i])
        for j in range(0,r+1):
            print(l[j])
while(1):
    c=int(input("enter your choice "))
    if(c==0):
        break
    if(c==1):
        data=int(input("enter data for enqueue "))
        r=Enqueue(data,f,r)
        if(f==-1 and r==0):
            f=0
    if(c==2):
        f=Dequeue(f,r)
        if(f==-1):
            r=-1
    if(c==3):
        display(f,r)
    
