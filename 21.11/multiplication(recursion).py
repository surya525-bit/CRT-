def multi(i,j):
    if(j!=0):
        j-=1
        multi(i,j)
        print(i*(j+1))
    else:
        return
i=int(input())
j=int(input())
multi(i,j)
