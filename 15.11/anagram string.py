'''s1=input()
s2=input()
d1={}
c=0
for i in s1:
    if i not in d1.keys():
        d1[i]=1
    else:
        d1[i]+=1
for i in s2:
    d1[i]-=1
for i in d1.values():
    if(i!=0):
        c+=1
        break
if(c==0 and len(s1)==len(s2)):
    print("anagram")
else:
    print("not anagram")'''

f=[0]*26
s1=input().lower()
s2=input().lower()
for i in s1:
    f[ord(i)-97]+=1
for i in s2:
    f[ord(i)-97]-=1
w=0
for i in f:
    if(i!=0):
        w=1
        break
if(w==1):
    print("not anagram")
else:
    print("anagram")
    
