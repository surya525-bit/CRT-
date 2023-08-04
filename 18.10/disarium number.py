n=input()
k=0
j=1
for i in range(len(n)):
    k=((int(n[i]))**j)+k
    j=j+1
if (int(k)==int(n)):
    print("disarium number")
else:
    print("not a disarium number")
