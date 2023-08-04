class node:
    def __init__(self,data):
        self.data=data
        self.address=None
head=None
def insert_at_bg(head,data):
    t=node(data)
    if(head==None):
        head=t
    else:
        t.address=head
        head=t
    return head
def display(head):
    p=head
    if(p==None):
        print("No Nodes")
        return
    else:
            print(p.data)
            p=p.address
            if(p!=None):
                display(p)
while(1):
    print("ch1: insert","ch2: display","ch3: exit",sep="     ")
    ch=int(input())
    if(ch==1):
        data=int(input("data:"))
        head=insert_at_bg(head,data)
    elif(ch==2):
        display(head)
    elif(ch==3):
        break
    else:
        print("INVALID CHOICE")

        
