s="abcdabcdaaaaaabbbbbbcccccc"
k=int(input())
i=0
j=0
d={}
count=0
c=0
while(j<len(s)):
    if(len(d)<=k):
        if(s[j] not in d.keys()):
            d[s[j]]=1
        else:
            d[s[j]]+=1
    if(len(d)>k or j==len(s)):
        if((j-i)>count):
              count=j-i
        while(len(d)>k):
            d[s[i]]-=1
            if(d[s[i]]==0):
                d.pop(s[i])
            i+=1
    j+=1
    if(len(d)==k and j==len(s)):
        if((j-i)>count):
              count=j-i
print(count)
