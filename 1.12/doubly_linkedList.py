class doublylinkedlist:
    def __init__(self,data):
        self.data=data
        self.address=None
        self.prev=None
head=None
tail=None
def insert_at_bg(head,data):
    l=doublylinkedlist(data)
    if(head==None):
        head=l
        tail=l
    else:
        l.address=head
        head=l
        l1=l.address
        l1.prev=l
    return head
def insert_at_end(tail,data):
    l=doublylinkedlist(data)
    p=tail
    if(tail==None):
        tail=l
        head=l
    else:
        p.address=l
        l.prev=p
        tail=l
    return tail
def delete_at_end(head,tail):
    if(head==tail):
        del head
        tail=None
    elif(head.address==tail):
        del tail
        head.address=None
        tail=head
    else:
        head=head.address
        if(head!=None):
            tail=delete_at_end(head,tail)
    return tail
    
    
def display(tail):
    p=tail
    if(p==None):
        print("Empty List")
        return
    else:
        print(p.data)
        p=p.prev
        if(p!=None):
            display(p)

while(1):
    c=int(input("Enter your choice"))
    if(c==1):
        data=int(input("enter the data "))
        head=insert_at_bg(head,data)
        if(tail==None):
            tail=head
    if(c==2):
        data=int(input("Enter the data"))
        tail=insert_at_end(tail,data)
        if(head==None):
            head=tail
    if(c==3):
        tail=delete_at_end(tail,data)
    if(c==0):
        display(tail)
    
