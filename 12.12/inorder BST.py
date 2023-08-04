#l=[90,85,35,140,99,11,26,35,118,40,60,58,56,83]
class BST:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=None
def insert(data,p):
    if(p==None):
        l=BST(data)
        root=l
        return root
    else:
        if(data<p.data):
            if(p.left==None):
                l=BST(data)
                p.left=l
                return p
            else:
                p.left=insert(data,p.left)
                return p
        elif(data>p.data):
            if(p.right==None):
                l=BST(data)
                p.right=l
                return p
            else:
                p.right=insert(data,p.right)
                return p
def inorder(root):
    p=root
    if(p==None):
        print("Tree is empty")
        return
    if(p.left!=None):
        inorder(p.left)
    print(p.data)
    if(p.right!=None):
        inorder(p.right)

def postorder(root):
    p=root
    if(p==None):
        print("Tree is empty")
        return
    else:
        if(p.left!=None):
            postorder(p.left)
        if(p.right!=None):
            postorder(p.right)
        print(p.data)

def preorder(root):
    p=root
    if(p==None):
        print("Tree is empty")
        return
    else:
        print(p.data)
        if(p.left!=None):
            preorder(p.left)
        if(p.right!=None):
            preorder(p.right)
def delete(root,data):
    p=root
    if(data<p.data):
        p.left=delete(p.left,data)
    elif(data>p.data):
        p.right=delete(p.right,data)
    elif(p.data==data):
        if(p.left==None):
            return p.right
        elif(p.right==None):
            return p.left
        elif(p.right!=None and p.left!=None):
            q=p
            q=q.right
            p.data=delete(p,p.data+1)
            return p.data
    return p
            
while(1):
    c=int(input("enter choice "))
    if(c==1):
        data=list(map(int,input("enter data").split()))
        for i in data:
            root=insert(i,root)
    elif(c==2):
        inorder(root)
    elif(c==3):
        preorder(root)
    elif(c==4):
        postorder(root)
    elif(c==5):
        data=int(input("Enter data to be deleted"))
        delete(root,data)
    elif(c==0):
        break
