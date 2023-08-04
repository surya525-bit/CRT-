n=int(input("Enter the size of stack "))
l=[0]*n
top=-1
def push(data,top,n):
    if(top==n-1):
        print("overflow")
    else:
        top=top+1
        l[top]=data
    return top
def pop(top):
    if(top==-1):
        print("underflow")
    else:
        print(l[top])
        top=top-1
    return top
    
def display(top):
    for i in range(top+1):
        print(l[i])
while(1):
    c=int(input("Enter your choice "))
    if(c==0):
        break
    elif(c==1):
        data=int(input("Enter the data to Push into stack "))
        top=push(data,top,n)
    elif(c==2):
        top=pop(top)
    elif(c==3):
        display(top)
        
