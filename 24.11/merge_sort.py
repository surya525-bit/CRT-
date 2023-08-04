#Merge
def merge(arr,i,m,j):
    nl1=m-i+1
    nl2=j-m
    l1=arr[i:m+1]
    l2=arr[m+1:j+1]
    r=[]
    p=0
    q=0
    while(q<len(l2) or p<len(l1)):
        if(q==len(l2)):
            r.append(l1[p])
            p+=1
        elif(p==len(l1)):
            r.append(l2[q])
            q+=1
        elif(l2[q]>l1[p]):
            r.append(l1[p])
            p+=1
        elif(l1[p]>=l2[q]):
            r.append(l2[q])
            q+=1
    return r
#Merge_sort
def merge_sort(arr,i,j):
    if(i==j):
        return
    else:
        m=(i+j)//2
        merge_sort(arr,i,m)
        merge_sort(arr,m+1,j)
        arr[i:j+1]=merge(arr,i,m,j)
        return arr
arr=[5,3,1,7,9,6,2,8,55]
i=0
j=len(arr)-1
print(merge_sort(arr,i,j))
