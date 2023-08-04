class linkedlist:
    def __init__(self,data):
        self.data=data
        self.address=None
head=None
tail=None
head1=None
tail1=None
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
def delete_at_bg(head):
    p=head
    if(p!=None):
        head=p.address
        p.address=None
        del p
    else:
        print("no node to delete")
    return head
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
def insert_at_spec(head,data,pos,tail):
    c=0
    d=linkedlist(data)
    p=head
    if(p==None):
        head=d
        tail=d
        return head
    elif(pos==1):
        if(head==None):
            head=l
            tail=l
        else:
            d.address=head
            head=d
        return head
    else:
        while(p.address!=None):
            if(c==pos-2):
                d.address=p.address
                p.address=d
            p=p.address
            c+=1
        if(c+2==pos):
            tail.address=d
            tail=d
        return tail
def delete_at_spec(head,tail,pos):
    p=head
    c=0
    if(p==None):
        print("no node to delete")
    elif(pos==1):
        head=p.address
        p.address=None
        del p
        return head
    else:
        while(p.address!=None):
            if(c==pos-2):
                q=p.address
                p.address=q.address
            p=p.address
            c+=1
        return tail
def displayreverse(head):
    p=head
    if(p==None):
        return
    else:
        t=p.data
        p=p.address
        if(p!=None):
            displayreverse(p)
            print(t)
        else:
            print(t)
        return
def reverse_list(head,tail):
    p1=head
    p2=p1.address
    p3=p2.address
    while(p3!=None):
        if(p1==head and p1.address!=None):
            p1.address=None
        if(p3!=None):
            p2.address=p1
            p1=p2
            p2=p3
            p3=p3.address
    p2.address=p1
    head=p2
    return head
def number_of_elements(head):
    c=0
    p=head
    while(1):
        c+=1
        if(p.address==None):
            break
        else:
            p=p.address
    return c
def display_middle(head):
    a=number_of_elements(head)
    c=0
    p=head
    if(a%2==0):
        while(c<=((a//2)+1)):
            c+=1
            if(c==a//2 or c==(a//2)+1):
                print(p.data)
            p=p.address
    else:
        while(c<=((a//2)+1)):
            c+=1
            if(c==(a//2)+1):
                print(p.data)
            p=p.address
def another_LL(head1,tail1,data):
    l=linkedlist(data)
    if(head1==None):
        head1=l
        tail1=l
    else:
        tail1.address=l
        tail1=l
    return tail1
def linking_linked_list(head1,tail1,head,tail):
    p=tail
    p.address=head1
    tail=tail1
    return head
                
          
while(1):
    print('1.insert_at_bg','2.insert_at_end','3.insert_at_spec','4.dele_at_bg','5.delete_at_end','6.delete_at_spec','7.display',
          '8.displayreverse','9.reverse_list','10.number_of_elements','11.print_middle','12.another_LL','13.linking_linked_list','100.exit',sep="\t")
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
        data=int(input("enter the data "))
        pos=int(input("enter the position "))
        if(pos==1):
            head=insert_at_spec(head,data,pos,tail)
            if(head==None):
                 tail=None
        else:
            tail=insert_at_spec(head,data,pos,tail)
            if(tail==None):
                 head=None
    elif(c==4):
        head=delete_at_bg(head)
        if(head==None):
            tail=None
    elif(c==5):
        tail=delete_at_end(head,tail)
        if(tail==None):
            head=None
    elif(c==6):
        pos=int(input("enter the position"))
        if(pos==1):
            head=delete_at_spec(head,tail,pos)
            if(head==None):
                tail=None
        else:
            tail=delete_at_spec(head,tail,pos)
            if(tail==None):
                head=None
    elif(c==7):
        k=int(input("choose list 1/2"))
        if(k==1):
            display(head)
        if(k==2):
            display(head1)
    elif(c==8):
        displayreverse(head)
    elif(c==9):
        k=head
        head=reverse_list(head,tail)
        tail=k
    elif(c==10):
        a=number_of_elements(head)
        print(a)
    elif(c==11):
        display_middle(head)
    elif(c==12):
        data=int(input("Enter Data"))
        tail1=another_LL(head1,tail1,data)
        if(head1==None):
            head1=tail1
    elif(c==13):
        head=linking_linked_list(head1,tail1,head,tail)
    elif(c==100):
        break
    else:
        print("invalid")
        break
