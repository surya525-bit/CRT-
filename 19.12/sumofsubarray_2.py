l=list(map(int,input().split()))
w=int(input())
s=[]
def sum_of_subarray(l,w,s):
    if(len(l)==0 or w==0):
        p=sum(s)
        return p
    elif(w>=l[0]):
        t=sum_of_subarray(l[1:],w,s)
        t1=sum_of_subarray(l[1:],w-l[0],s.append(l[0]))
        m=max(t,t1)
        if(m==None):
            return 0
        else:
            return m
    elif(w<l[0]):
        t=sum_of_subarray(l[1:],w,s)
        return t
s=sum_of_subarray(l,w,s)
print(s)
