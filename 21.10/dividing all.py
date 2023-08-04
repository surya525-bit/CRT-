import math
l=list(map(int,input().split()))
for j in l:
    for i in range(2,j+1):
        if(j%i==0):
            break
        print(i+1)
    print()
'''if(n!=0):
    for i in range(2,a+1):
        if(n%i==0):
            c=c+1
    if(c==0):
    print("prime")'''
