a=int(input())
b=int(input())
def rev(p):
    s=0
    while(p!=0):
        r=p%10
        s=(s*10)+r
        p=p//10
    return s
c=a+b
if(rev(a)+rev(b)==rev(c)):
    print("energetic")
else:
    print("not")
