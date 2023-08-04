class circular_linkedlist:
    def __init__(self,data):
        self.data=data
        self.address=None
head=None
tail=None

def insert_at_end(tail,data):
    p=tail
    l=circular_linkedlist(data)
    if(tail==None):
        l.address=l
        tail=l
    else:
        l.address=p.address
        p.address=l
        tail=l
    return tail
def insert_at_bg(tail,data):
    p=tail
    l=circular_linkedlist(data)
    if(tail==None):
        l.address=l
        tail=l
    else:
        l.address=p.address
        p.address=l
    return tail
def insert_at_spec(tail,pos,data):
    l=circular_linkedlist(data)
    p=tail
    c=0
    if(pos<=0):
        print("Invalid position")
    elif(pos>0):
        while(c+1<pos or p!=tail)
            p=p.address
            c+=1
        
        l.address=p.address
        p.address=l
    return
    

def delete_at_end(tail):
    p=tail
    if(p==None):
        return
    elif(p.address==p):
        del p
        tail=None
    else:
        while(p.address!=tail):
            p=p.address
        q=tail
        p.address=q.address
        tail=p
        q.address=None
        del q
    return tail

def display(tail):
    p=tail
    if(p==None):
        print("Empty List")
    else:
        p=p.address
        while(p!=tail):
            print(p.data)
            p=p.address
        print(p.data)
        
while(1):
    c=int(input("enter your choice"))
    if(c==1):
        data=int(input("enter data"))
        tail=insert_at_end(tail,data)
    if(c==2):
        data=int(input("enter data "))
        tail=insert_at_bg(tail,data)
    if(c==3):
        data=int(input("enter data "))
        pos=int(input("enter position"))
        insert_at_spec(tail,pos,data)
    if(c==3):
        tail=delete_at_end(tail)
        
    elif(c==0):
        display(tail)
        
        
        
