l=list(map(int,input().split()))
k=int(input())
def delete(l,k,i):
    if(k!=l[i]):
        i-=1
        delete(l,k,i)
        return l
    else:
        l.pop(i)
        return
print(delete(l,k,len(l)-1))
