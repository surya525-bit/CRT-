s="India is my country"
def rev_str(str):
    str1=" "
    for i in range(len(str)-1,-1,-1):
        str1=str1+str[i]
    return str1
print(rev_str(s))
def rev_strs(str):
    str2=" "
    for i in range(len(str)):
        if(s[i]!=" "):
            str2=str2+s[i]
        else:
            print(rev_str(str2),end=" ")
            str2=""
        if(i==len(str)-1):
            print(rev_str(str2),end=" ")
    print()
rev_strs(s)
