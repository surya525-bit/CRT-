def fun(i):
    if(i==0):
        return 10
    else:
        print("surya")
        i=i-1
    r=fun(i)
    print(r)
    return r+1
fun(5)
