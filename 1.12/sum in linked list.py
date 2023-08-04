'''import math
class linkedlist:
    def __init__(self,data):
        self.data=data
        self.address=None
l1=[]
l2=[]
l3=[]
head=None
tail=None
head1=None
head2=None
tail1=None
tail2=None
def insert_at_end(tail,head,data):
    l=linkedlist(data)
    if(tail==None):
        tail=l
        head=l
    else:
        tail.address=l
        tail=l
    return tail
def display(head,l):
    p=head
    if(p==None):
        print("Empty List")
        return 
    else:
        l.append(p.data)
        p=p.address
        if(p!=None):
            display(p,l)
        return l
def sum(head,head1,l1,l2,tail2,head2):
    for i in range(len(l1)-1):
        k1=str(l1[i])+str(l1[i+1])
        print(k1)
    for i in range(len(l2)-1):
        k2=str(l2[i])+str(l2[i+1])
        print(k2) 
    k3=int(k1) + int(k2)
    print(k3)
    c=int(math.log(k3,10))+1
    print(c)
    for i in range(c):
        r=k3%10
        tail2=insert_at_end(tail2,head2,r)
        if(head2==None):
            head2=tail2
        k3=k3//10

    return tail2,head2
            
while(1):
    c=int(input("enter your choice"))
    if(c==1):
        k=int(input("enter list number"))
        if(k==1):
            data=int(input("enter the data "))
            tail=insert_at_end(tail,head,data)
            if(head==None):
                head=tail
        if(k==2):
            data=int(input("enter the data "))
            tail1=insert_at_end(tail1,head1,data)
            if(head1==None):
                head1=tail1
        if(k==3):
            data=int(input("enter the data "))
            tail2=insert_at_end(tail2,head2,data)
            if(head2==None):
                head2=tail2
    if(c==2):
        k=int(input("enter list number"))
        l=[]
        if(k==1):
          l1=display(head,l)
          print(l)
        if(k==2):
          l2=display(head1,l)
          print(l)
        if(k==3):
          l3=display(head2,l)
          print(l)
    if(c==3):
        m=sum(head,head1,l1,l2,tail2,head2)
        tail2=m[0]
        head2=m[1]
      '''
class linkedlist:
    def __init__(self,value):
        self.value=value
        self.address=None
head=None
tail=None
head1=None
tail1=None
head2=None
tail2=None
def insert(head,tail,value):
    l=linkedlist(value)
    if(head==None):
        head=l
        tail=l
    else:
        tail.address=l
        tail=l
    return tail
def display(head):
    p=head
    if(p==None):
        print("\nLinkedList is empty\n")
        return
    else:
        print(p.value)
        p=p.address
        if(p!=None):
            display(p)
def reverselist(head,tail):
    p=head
    q=tail
    if(head==None and tail==None):
        print("\nlinked list is empty\n")
        return
    if(p==q):
        return
    t=p.address
    t1=t.address
    while(t!=None):
        if(p==head):
            p.address=None
            t.address=p
            p=t
            t=t1
        else:
            t1=t.address
            t.address=p
            p=t
            t=t1
    head=p
    return head
def addinglist(p,q,qu,head2,tail2):
    while(p!=None and q!=None):
        a=p.value + q.value + qu
        qu=a//10
        r=a%10
        tail2=insert(head2,tail2,r)
        if(head2==None):
            head2=tail2
        p=p.address
        q=q.address
    if(p==None and q!=None):
        b=q.value+qu
        while(b!=0):
            r=b%10
            tail2=insert(head2,tail2,r)
            b=b//10
    elif(p!=None and q==None):
        b=p.value+qu
        while(b!=0):
            r=b%10
            tail2=insert(head2,tail2,r)
            b=b//10
    elif(qu<10):
        tail2=insert(head2,tail2,qu)
    else:
        while(qu!=0):
            r=qu%10
            tail2=insert(head2,tail2,r)
            qu=qu//10
    return head2,tail2
while(1):
    a=int(input("\nenter the list number \n"))
    if(a==1):
        print('1.insert','2.display',sep="\n")
        print('3.reverselist','4.exit',sep="\n")
        c=int(input("choose your choice "))
        if(c==1):
            value=int(input("enter the value "))
            tail=insert(head,tail,value)
            if(head==None):
                head=tail
        elif(c==2):
            display(head)
        elif(c==3):
            k=head
            head=reverselist(head,tail)
            tail=k
        elif(c==4):
            break
        else:
            print("Invalid choice")
            break
    elif(a==2):
        print('1.insert','2.display',sep="\n")
        print('3.reverselist','4.exit',sep="\n")
        c=int(input("choose your choice "))
        if(c==1):
            value=int(input("enter the value "))
            tail1=insert(head1,tail1,value)
            if(head1==None):
                head1=tail1
        elif(c==2):
            display(head1)
        elif(c==3):
            k=head1
            head1=reverselist(head1,tail1)
            tail1=k
        elif(c==4):
            break
        else:
            print("Invalid choice")
            break
    elif(a==3):
        l=addinglist(head,head1,0,head2,tail2)
        l=list(l)
        head2=l[0]
        tail2=l[1]
    elif(a==4):
        k=head2
        head2=reverselist(head2,tail2)
        tail2=k
        display(head2)
    
    







        
        

