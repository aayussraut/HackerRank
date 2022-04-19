def theLoveLetterMystery(s):
    count=0
    length=len(s)//2 if len(s)%2==0 else len(s)//2+1
    # print(length)
    for i in range(length):
        count+=abs(ord(s[-1-i])-ord(s[i]))
    # print(count)
    return(count)

# s="abcd"
# s="abcde"
# s="cba"
s="abcba"
theLoveLetterMystery(s)