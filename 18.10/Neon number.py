n=int(input())
a=n*n
a=str(a)
k=0
print(a)
for i in range(len(a)-1):
    k=int(a[i])+int(a[i+1])
if (k==n):
    print("neon number")
else:
    print("not a neon number")
           
    
