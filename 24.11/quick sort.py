def quick_sort(l,i,j):
    l=[1,2]
    p=l[0]
    i=1
    j=len(l)-1
    while(i<j):
        if(l[i]<p):
            i+=1
        if(l[i]>p):
            if(l[j]>p):
                j-=1
            if(l[j]<p):
                t=l[i]
                l[i]=l[j]
                l[j]=t
                i+=1
                j-=1
        c=p
        l[0]=l[j]
        l[j]=c
    print(l)
    print(i)

