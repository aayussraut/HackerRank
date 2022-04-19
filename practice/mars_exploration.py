def marsExploration(s):
    count=0
    length=len(s)//3
    msg=""
    for i in range(length):
        msg+="SOS"
    for i in range(len(s)):
        if s[i]!=msg[i]:
            count+=1
    print(count)
s="SOSSPSSQSSOR"
marsExploration(s)