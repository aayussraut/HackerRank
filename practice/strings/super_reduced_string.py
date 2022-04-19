def superReducedString(s):
    s=list(s)
    i=0
    while(i<=len(s)-2):
        if s[i]==s[i+1]:
            del s[i]
            del s[i]
            if i!=0:
                i-=1
        else:
            i+=1
    if len(s)==0:
        print("Empty String")
        return ("Empty String")
    print("".join(s))



s="baab"
superReducedString(s)