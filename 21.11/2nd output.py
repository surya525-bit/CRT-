def fun(n,t):
    if(n==1):
        return t
    else:
        print(n,t)
        x=fun(n-1,(n-1)*t)
        print(x)
        return x
print(fun(4,4))
