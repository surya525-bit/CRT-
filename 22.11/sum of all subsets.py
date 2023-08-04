op=[0]
op1=[0]
op2=[0]
ip=list(map(int,input().split()))
l=[]
def subset(ip,op,l):
    if(len(ip)==0):
        l.append(op)
        return
    else:
        op1[0]=op[0]+ip[0]
        op2[0]=op2.append(op[0])
        ip=ip[1:]
        subset(ip,op1,l)
        subset(ip,op2,l)
        return
subset(ip,op,l)
print(l)

    
