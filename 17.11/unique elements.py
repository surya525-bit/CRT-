s="aabcadaabde"
i=0
j=0
s1=[]
while(j<len(s)):
    if(s[j] not in s1):
        s1.append(s[j])
        if((a-b) < (j-i)):
            a=i
            b=j
    else:
        s1.pop(i)
        i+=1
    j+=1
print(a,b,end=" ")
        
        
