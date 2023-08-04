l=list(map(int,input().split()))
def delete(l,i):
    le=len(l)
    if(le%2==0):
        h=le//2
    else:
        h=(le//2)+1
    if(h!=l[i]):
        i-=1
        delete(l,i)
        return l
    else:
        l.pop(i)
        return
print(delete(l,len(l)-1))
