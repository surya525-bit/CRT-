s=int(input())
l=list(map(int,input().split()))
op=[]
def sumod(l,op,s):
    if(len(l)==0):
        if(sum(op)==s):
            print(op)
        return
    else:
        op1=op.copy()
        op2=op.copy()
        op2.append(l[0])
        l=l[1:]
        sumod(l,op1,s)
        sumod(l,op2,s)
        return
sumod(l,op,s)


    
