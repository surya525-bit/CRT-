def subset(ip,op,l):
    if(len(ip)==0):
        l.append(op)
        return
    else:
        op1=op
        op2=op+ip[0]
        ip=ip[1:]
        subset(ip,op1,l)
        subset(ip,op2,l)
        return
s=list(map(int,input().split()))
l=[]
subset(s," ",l)
print(set(l))
