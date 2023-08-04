class linkedlist:
    def __init__(self,data):
        self.data=data
        self.address=None
head=None
tail=None
def insert_at_bg(head,data):
    l=linkedlist(data)
    if(head==None):
        head=l
        tail=l
    else:
        l.address=head
        head=l
    return head
def insert_at_end(head,tail,data):
    l=linkedlist(data)
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
        print("Empty List")
        return
    else:
        print(p.data)
        p=p.address
        if(p!=None):
            display(p)
def checking_for_loop(head):
    p=head
    q=head
    c=0
    while(1):
        if(c==0):
            p=p.address
            q=q.address
            q=q.address
            c=1
        if(p.address==None or q.address==None):
            print("No loop")
            break
        if(p==q and c==1):
            print("list is looped")
            break
        if(p!=q and c==1):
            p=p.address
            q=q.address
            q=q.address
            

while(1):
    c=int(input("choose your choice "))
    if(c==1):
        data=int(input("enter the data "))
        head=insert_at_bg(head,data)
        if(tail==None):
            tail=head
    elif(c==2):
        data=int(input("enter the data "))
        tail=insert_at_end(head,tail,data)
        if(head==None):
            head=tail
    elif(c==3):
        p=tail
        p.address=head
    elif(c==4):
        checking_for_loop(head)
    
    elif(c==7):
        display(head)
