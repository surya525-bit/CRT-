n=int(input())
def order(i,j):
    if(i<=j):
        print(i)
        i+=1
        order(i,j)
        print(i-1)
    else:
        return
order(1,n)
