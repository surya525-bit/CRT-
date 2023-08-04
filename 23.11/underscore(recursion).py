def underscore(ip,op):
    if(len(ip)==0):
        print(op)
        return
    else:
        op1=op+"_"+ip[0]
        op2=op+ip[0]
        ip=ip[1:]
        underscore(ip,op1)
        underscore(ip,op2)
        return
s="abc"
op="a"
underscore(s[1:],op)

'''
def underscore(ip,op):
    if(len(ip)==0):
        print(op)
        return
    else:
        op1=ip[-1]+"_"+op
        op2=ip[-1]+op
        ip=ip[:len(ip)-1]
        underscore(ip,op1)
        underscore(ip,op2)
        return
s="abc"
op="c"
underscore(s[:len(s)-1],op)
    '''
    
