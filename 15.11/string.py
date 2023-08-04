s=input()
c=0
dict={}
for i in range(len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=90):
        continue
    elif(ord(s[i])>=97 and ord(s[i])<=122):
        continue
    elif(ord(s[i])>=48 and ord(s[i])<=57):
        continue
    else:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
for i in dict.keys():
    print(i,"->",dict[i])
