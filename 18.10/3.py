n=int(input())

for i in range(1,n+1):
    p=i*2
    for j in range(1,n+1):
        if(p<10):
            print("0",p," ",end=" ",sep="")
        else:
            print(p," ",end=" ",sep="")
        p*=2
    print()
