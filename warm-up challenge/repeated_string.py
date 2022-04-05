


def repeatedString(s, n):
    count=0
    extra=0
    count+=s.count('a')
    toRepeat=n//len(s)
    print(toRepeat)
    left=n-(toRepeat*len(s))
    print(left)
    for i in range(left):
        extra=s[:left].count("a")
    repeated=(toRepeat*count)+extra
    print(repeated)



n=10
s="aba"
repeatedString(s,n);